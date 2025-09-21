import json
import math
from functools import cache
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

import numpy as np


@dataclass
class TextureMetadata:
  width: int
  height: int
  depth: int
  pixel_format: str
  bytes_per_pixel: int
  total_bytes: int


@dataclass
class Texture:
  meta: TextureMetadata
  data: np.ndarray # stored as (Depth, Height, Width, Channels)


def _read_metadata(json_path: Path) -> TextureMetadata:
  with open(json_path, "r", encoding="utf-8") as f:
    m = json.load(f)
  return TextureMetadata(
    width=int(m["Width"]),
    height=int(m["Height"]),
    depth=int(m["Depth"]),
    pixel_format=str(m["PixelFormat"]),
    bytes_per_pixel=int(m["BytesPerPixel"]),
    total_bytes=int(m["TotalBytes"]),
  )


def _decode_r11g11b10_uint_to_float_rgb(packed: np.ndarray) -> np.ndarray:
  """Decode DXGI_R11G11B10_FLOAT (aka FloatR11G11B10) to float32 RGB.

  packed: np.ndarray of dtype uint32, shape (...,)
  returns float32 array of shape (..., 3)
  """
  # Bit layout (least significant bit on the right):
  # R: bits [0..10]  -> 11-bit float (5-bit exponent, 6-bit mantissa)
  # G: bits [11..21] -> 11-bit float (5-bit exponent, 6-bit mantissa)
  # B: bits [22..31] -> 10-bit float (5-bit exponent, 5-bit mantissa)
  r_bits = (packed >> 0) & np.uint32(0x7FF)   # 11 bits
  g_bits = (packed >> 11) & np.uint32(0x7FF)  # 11 bits
  b_bits = (packed >> 22) & np.uint32(0x3FF)  # 10 bits

  def _decode_component(bits: np.ndarray, mantissa_bits: int) -> np.ndarray:
    exp_bits = bits >> mantissa_bits
    mant_bits = bits & ((1 << mantissa_bits) - 1)
    bias = 15

    # Subnormal: exp == 0 -> value = 2^(-14) * mantissa / 2^mantissa_bits
    subnormal = exp_bits == 0
    normal = (exp_bits > 0) & (exp_bits < 31)

    value = np.zeros_like(bits, dtype=np.float32)
    if np.any(subnormal):
      value[subnormal] = (2.0 ** -14) * (mant_bits[subnormal].astype(np.float32) / (2 ** mantissa_bits))
    if np.any(normal):
      value[normal] = (1.0 + mant_bits[normal].astype(np.float32) / (2 ** mantissa_bits)) * (
        2.0 ** (exp_bits[normal].astype(np.int32) - bias)
      )
    # exp == 31 (all ones): treat as large value; clamp to finite max representable approx.
    # Using the largest finite value for this limited-precision float representation.
    special = exp_bits == 31
    if np.any(special):
      # Max finite for 11-bit mantissa (~2^(16) * (1 + 63/64)) and for 10-bit (~2^(16) * (1 + 31/32)).
      # This branch should be rare in content; set to a plausible large number.
      max_finite = np.float32(65536.0)
      value[special] = max_finite
    return value

  r = _decode_component(r_bits, mantissa_bits=6)
  g = _decode_component(g_bits, mantissa_bits=6)
  b = _decode_component(b_bits, mantissa_bits=5)
  return np.stack([r, g, b], axis=-1)


def _reshape_tex(flat: np.ndarray, meta: TextureMetadata, channels: int) -> np.ndarray:
  # Assume X (width) is fastest-varying, then Y (height), then Z (depth)
  # so the memory order is: for z in [0..D-1], for y in [0..H-1], for x in [0..W-1]
  expected_pixels = meta.width * meta.height * meta.depth
  if flat.shape[0] != expected_pixels:
    raise ValueError(f"Pixel count mismatch: got {flat.shape[0]}, expected {expected_pixels}")
  return flat.reshape((meta.depth, meta.height, meta.width, channels))


@cache
def load_texture(bin_path: str | Path, json_path: Optional[str | Path] = None) -> Texture:
  """Load a texture from .bin and .json metadata.

  - Supports PixelFormat: "R8G8B8A8", "R8G8B8A8_UINT", "R8", "R32_FLOAT", "FloatR11G11B10".
  - Returns data as float32 in range [0,1] for UNORM formats, float32 for float formats.
  - Data layout: (D, H, W, C)
  """
  bin_p = Path(bin_path)
  if json_path is None:
    json_p = bin_p.with_suffix(".json")
  else:
    json_p = Path(json_path)

  meta = _read_metadata(json_p)

  # Read raw bytes
  raw = np.fromfile(bin_p, dtype=np.uint8)
  if raw.nbytes != meta.total_bytes:
    # Allow if file is larger due to alignment, but still matches leading expected size
    if raw.nbytes < meta.total_bytes:
      raise ValueError(f"Binary size {raw.nbytes} < metadata TotalBytes {meta.total_bytes}")
    raw = raw[: meta.total_bytes]

  pf = meta.pixel_format.upper()

  if pf in ("R8G8B8A8", "R8G8B8A8_UINT"):
    flat = raw.reshape((-1, 4)).astype(np.float32) / 255.0
    data = _reshape_tex(flat, meta, channels=4)
  elif pf == "R8":
    flat = raw.astype(np.float32) / 255.0
    data = _reshape_tex(flat[:, None], meta, channels=1)
  elif pf == "R32_FLOAT":
    if meta.bytes_per_pixel != 4:
      raise ValueError("R32_FLOAT must have 4 BytesPerPixel")
    flat = np.frombuffer(raw.tobytes(), dtype=np.float32).reshape((-1, 1))
    data = _reshape_tex(flat, meta, channels=1)
  elif pf == "FLOATR11G11B10":
    if meta.bytes_per_pixel != 4:
      raise ValueError("FloatR11G11B10 must have 4 BytesPerPixel")
    flat_u32 = np.frombuffer(raw.tobytes(), dtype=np.uint32)
    flat = _decode_r11g11b10_uint_to_float_rgb(flat_u32)
    data = _reshape_tex(flat, meta, channels=3)
  else:
    raise NotImplementedError(f"Unsupported PixelFormat: {meta.pixel_format}")

  return Texture(meta=meta, data=data.astype(np.float32, copy=False))



def load_texture_by_name(tex_dir: str | Path, tex_name: str) -> Texture:
  tex_path = Path(tex_dir) / tex_name
  bin_path = str(tex_path) + ".bin"
  json_path = str(tex_path) + ".json"
  return load_texture(bin_path, json_path)


def _clamp(x, low, high) -> float:
  return max(low, min(x, high))


def _lerp(a: np.ndarray, b: np.ndarray, t: float) -> np.ndarray:
  return a * (1.0 - t) + b * t


def _sample_trilinear(tex: Texture, u: float, v: float, w: float) -> np.ndarray:
  depth, height, width, channels = tex.data.shape

  # Map into texel space
  x = _clamp(u * width - 0.5, 0.0, float(width - 1))
  y = _clamp(v * height - 0.5, 0.0, float(height - 1))
  z = _clamp(w * depth - 0.5, 0.0, float(depth - 1))

  x0 = int(math.floor(x))
  y0 = int(math.floor(y))
  z0 = int(math.floor(z))

  x1 = min(x0 + 1, width - 1)
  y1 = min(y0 + 1, height - 1)
  z1 = min(z0 + 1, depth - 1)

  tx = float(x - x0)
  ty = float(y - y0)
  tz = float(z - z0)

  c000 = tex.data[z0, y0, x0]
  c100 = tex.data[z0, y0, x1]
  c010 = tex.data[z0, y1, x0]
  c110 = tex.data[z0, y1, x1]
  c001 = tex.data[z1, y0, x0]
  c101 = tex.data[z1, y0, x1]
  c011 = tex.data[z1, y1, x0]
  c111 = tex.data[z1, y1, x1]

  c00 = _lerp(c000, c100, tx)
  c10 = _lerp(c010, c110, tx)
  c01 = _lerp(c001, c101, tx)
  c11 = _lerp(c011, c111, tx)

  c0 = _lerp(c00, c10, ty)
  c1 = _lerp(c01, c11, ty)

  return _lerp(c0, c1, tz)


def sample_uv(
  tex: Texture,
  u: float,
  v: float,
  w: float
) -> np.ndarray:
  """Sample the texture at UV(W) in [0,1] using trilinear filtering.

  - Returns a float32 numpy array of shape (C,).
  """

  return _sample_trilinear(tex, u, v, w)
  