import enum

class EPixelFormat(enum.Enum):

  PF_Unknown              =0,
  PF_A32B32G32R32F        =1,
  PF_B8G8R8A8             =2,
  PF_G8                   =3, # G8  means Gray/Grey , not Green , typically actually uses a red format with replication of R to RGB
  PF_G16                  =4, # G16 means Gray/Grey like G8
  PF_DXT1                 =5,
  PF_DXT3                 =6,
  PF_DXT5                 =7,
  PF_UYVY                 =8,
  PF_FloatRGB             =9,  # FloatRGB == PF_FloatR11G11B10 , NOT 16F usually, but varies
  PF_FloatRGBA            =10, # RGBA16F
  PF_DepthStencil         =11,
  PF_ShadowDepth          =12,
  PF_R32_FLOAT            =13,
  PF_G16R16               =14,
  PF_G16R16F              =15,
  PF_G16R16F_FILTER       =16,
  PF_G32R32F              =17,
  PF_A2B10G10R10          =18,
  PF_A16B16G16R16         =19,
  PF_D24                  =20,
  PF_R16F                 =21,
  PF_R16F_FILTER          =22,
  PF_BC5                  =23,
  PF_V8U8                 =24,
  PF_A1                   =25,
  PF_FloatR11G11B10       =26,
  PF_A8                   =27,
  PF_R32_UINT             =28,
  PF_R32_SINT             =29,
  PF_PVRTC2               =30,
  PF_PVRTC4               =31,
  PF_R16_UINT             =32,
  PF_R16_SINT             =33,
  PF_R16G16B16A16_UINT    =34,
  PF_R16G16B16A16_SINT    =35,
  PF_R5G6B5_UNORM         =36,
  PF_R8G8B8A8             =37,
  PF_A8R8G8B8				      =38,	# Only used for legacy loading; do NOT use!
  PF_BC4					        =39,
  PF_R8G8                 =40,
  PF_ATC_RGB				      =41,  # Unsupported Format
  PF_ATC_RGBA_E			      =42,	# Unsupported Format
  PF_ATC_RGBA_I			      =43,	# Unsupported Format
  PF_X24_G8				        =44,	# Used for creating SRVs to alias a DepthStencil buffer to read Stencil. Don't use for creating textures.
  PF_ETC1					        =45,	# Unsupported Format
  PF_ETC2_RGB				      =46,
  PF_ETC2_RGBA			      =47,
  PF_R32G32B32A32_UINT	  =48,
  PF_R16G16_UINT			    =49,
  PF_ASTC_4x4             =50,	# 8.00 bpp
  PF_ASTC_6x6             =51,	# 3.56 bpp
  PF_ASTC_8x8             =52,	# 2.00 bpp
  PF_ASTC_10x10           =53,	# 1.28 bpp
  PF_ASTC_12x12           =54,	# 0.89 bpp
  PF_BC6H					        =55,
  PF_BC7					        =56,
  PF_R8_UINT				      =57,
  PF_L8					          =58,
  PF_XGXR8				        =59,
  PF_R8G8B8A8_UINT		    =60,
  PF_R8G8B8A8_SNORM		    =61,
  PF_R16G16B16A16_UNORM	  =62,
  PF_R16G16B16A16_SNORM	  =63,
  PF_PLATFORM_HDR_0		    =64,
  PF_PLATFORM_HDR_1		    =65,	# Reserved.
  PF_PLATFORM_HDR_2		    =66,	# Reserved.
  PF_NV12				        	=67,
  PF_R32G32_UINT          =68,
  PF_ETC2_R11_EAC			    =69,
  PF_ETC2_RG11_EAC		    =70,
  PF_R8		                =71,
  PF_B5G5R5A1_UNORM       =72,
  PF_ASTC_4x4_HDR         =73,
  PF_ASTC_6x6_HDR         =74,
  PF_ASTC_8x8_HDR         =75,
  PF_ASTC_10x10_HDR       =76,
  PF_ASTC_12x12_HDR       =77,
  PF_G16R16_SNORM		      =78,
  PF_R8G8_UINT			      =79,
  PF_R32G32B32_UINT		    =80,
  PF_R32G32B32_SINT		    =81,
  PF_R32G32B32F			      =82,
  PF_R8_SINT				      =83,
  PF_R64_UINT				      =84,
  PF_R9G9B9EXP5			      =85,
  PF_P010					        =86,
  PF_ASTC_4x4_NORM_RG		  =87, # RG format stored in LA endpoints for better precision (requires RHI support for texture swizzle)
  PF_ASTC_6x6_NORM_RG		  =88,
  PF_ASTC_8x8_NORM_RG		  =89,
  PF_ASTC_10x10_NORM_RG	  =90,
  PF_ASTC_12x12_NORM_RG	  =91,
  PF_R16G16_SINT			    =92,
  PF_R8G8B8				        =93,
  PF_MAX					        =94,

class FPixelFormatInfo():
  def __init__(
      self,
      UnrealFormat: EPixelFormat,
      Name: str,
      BlockSizeX: int,
      BlockSizeY: int,
      BlockSizeZ: int,
      BlockBytes: int,
      NumComponents: int,
      Supported: bool,
  ):
    self.UnrealFormat = UnrealFormat
    self.Name = Name
    self.BlockSizeX = BlockSizeX
    self.BlockSizeY = BlockSizeY
    self.BlockSizeZ = BlockSizeZ
    self.BlockBytes = BlockBytes
    self.NumComponents = NumComponents
    self.Supported = Supported

GPixelFormats = [
  #                             UnrealFormat           Name            BlockSizeX  BlockSizeY  BlockSizeZ  BlockBytes  NumComponents    Supported
  FPixelFormatInfo(EPixelFormat.PF_Unknown,            "unknown",               0,          0,          0,          0,          0,              0),
  FPixelFormatInfo(EPixelFormat.PF_A32B32G32R32F,      "A32B32G32R32F",         1,          1,          1,          16,         4,              1),
  FPixelFormatInfo(EPixelFormat.PF_B8G8R8A8,           "B8G8R8A8",              1,          1,          1,          4,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_G8,                 "G8",                    1,          1,          1,          1,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_G16,                "G16",                   1,          1,          1,          2,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_DXT1,               "DXT1",                  4,          4,          1,          8,          3,              1),
  FPixelFormatInfo(EPixelFormat.PF_DXT3,               "DXT3",                  4,          4,          1,          16,         4,              1),
  FPixelFormatInfo(EPixelFormat.PF_DXT5,               "DXT5",                  4,          4,          1,          16,         4,              1),
  FPixelFormatInfo(EPixelFormat.PF_UYVY,               "UYVY",                  2,          1,          1,          4,          4,              0),
  FPixelFormatInfo(EPixelFormat.PF_FloatRGB,           "FloatRGB",              1,          1,          1,          4,          3,              1),
  FPixelFormatInfo(EPixelFormat.PF_FloatRGBA,          "FloatRGBA",             1,          1,          1,          8,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_DepthStencil,       "DepthStencil",          1,          1,          1,          4,          1,              0),
  FPixelFormatInfo(EPixelFormat.PF_ShadowDepth,        "ShadowDepth",           1,          1,          1,          4,          1,              0),
  FPixelFormatInfo(EPixelFormat.PF_R32_FLOAT,          "R32_FLOAT",             1,          1,          1,          4,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_G16R16,             "G16R16",                1,          1,          1,          4,          2,              1),
  FPixelFormatInfo(EPixelFormat.PF_G16R16F,            "G16R16F",               1,          1,          1,          4,          2,              1),
  FPixelFormatInfo(EPixelFormat.PF_G16R16F_FILTER,     "G16R16F_FILTER",        1,          1,          1,          4,          2,              1),
  FPixelFormatInfo(EPixelFormat.PF_G32R32F,            "G32R32F",               1,          1,          1,          8,          2,              1),
  FPixelFormatInfo(EPixelFormat.PF_A2B10G10R10,        "A2B10G10R10",           1,          1,          1,          4,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_A16B16G16R16,       "A16B16G16R16",          1,          1,          1,          8,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_D24,                "D24",                   1,          1,          1,          4,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R16F,               "PF_R16F",               1,          1,          1,          2,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R16F_FILTER,        "PF_R16F_FILTER",        1,          1,          1,          2,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_BC5,                "BC5",                   4,          4,          1,          16,         2,              1),
  FPixelFormatInfo(EPixelFormat.PF_V8U8,               "V8U8",                  1,          1,          1,          2,          2,              1),
  FPixelFormatInfo(EPixelFormat.PF_A1,                 "A1",                    1,          1,          1,          1,          1,              0),
  FPixelFormatInfo(EPixelFormat.PF_FloatR11G11B10,     "FloatR11G11B10",        1,          1,          1,          4,          3,              0),
  FPixelFormatInfo(EPixelFormat.PF_A8,                 "A8",                    1,          1,          1,          1,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R32_UINT,           "R32_UINT",              1,          1,          1,          4,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R32_SINT,           "R32_SINT",              1,          1,          1,          4,          1,              1),

  # IOS Support
  FPixelFormatInfo(EPixelFormat.PF_PVRTC2,             "PVRTC2",                8,          4,          1,          8,          4,              0),
  FPixelFormatInfo(EPixelFormat.PF_PVRTC4,             "PVRTC4",                4,          4,          1,          8,          4,              0),

  FPixelFormatInfo(EPixelFormat.PF_R16_UINT,           "R16_UINT",              1,          1,          1,          2,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R16_SINT,           "R16_SINT",              1,          1,          1,          2,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R16G16B16A16_UINT,  "R16G16B16A16_UINT",     1,          1,          1,          8,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R16G16B16A16_SINT,  "R16G16B16A16_SINT",     1,          1,          1,          8,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R5G6B5_UNORM,       "R5G6B5_UNORM",          1,          1,          1,          2,          3,              0),
  FPixelFormatInfo(EPixelFormat.PF_R8G8B8A8,           "R8G8B8A8",              1,          1,          1,          4,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_A8R8G8B8,           "A8R8G8B8",              1,          1,          1,          4,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_BC4,                "BC4",                   4,          4,          1,          8,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R8G8,               "R8G8",                  1,          1,          1,          2,          2,              1),

  FPixelFormatInfo(EPixelFormat.PF_ATC_RGB,            "ATC_RGB",               4,          4,          1,          8,          3,              0),
  FPixelFormatInfo(EPixelFormat.PF_ATC_RGBA_E,         "ATC_RGBA_E",            4,          4,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ATC_RGBA_I,         "ATC_RGBA_I",            4,          4,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_X24_G8,             "X24_G8",                1,          1,          1,          1,          1,              0),
  FPixelFormatInfo(EPixelFormat.PF_ETC1,               "ETC1",                  4,          4,          1,          8,          3,              0),
  FPixelFormatInfo(EPixelFormat.PF_ETC2_RGB,           "ETC2_RGB",              4,          4,          1,          8,          3,              0),
  FPixelFormatInfo(EPixelFormat.PF_ETC2_RGBA,          "ETC2_RGBA",             4,          4,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_R32G32B32A32_UINT,  "PF_R32G32B32A32_UINT",  1,          1,          1,          16,         4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R16G16_UINT,        "PF_R16G16_UINT",        1,          1,          1,          4,          4,              1),

  # ASTC support
  FPixelFormatInfo(EPixelFormat.PF_ASTC_4x4,           "ASTC_4x4",              4,          4,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_6x6,           "ASTC_6x6",              6,          6,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_8x8,           "ASTC_8x8",              8,          8,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_10x10,         "ASTC_10x10",            10,         10,         1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_12x12,         "ASTC_12x12",            12,         12,         1,          16,         4,              0),

  FPixelFormatInfo(EPixelFormat.PF_BC6H,               "BC6H",                  4,          4,          1,          16,         3,              1),
  FPixelFormatInfo(EPixelFormat.PF_BC7,                "BC7",                   4,          4,          1,          16,         4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R8_UINT,            "R8_UINT",               1,          1,          1,          1,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_L8,                 "L8",                    1,          1,          1,          1,          1,              0),
  FPixelFormatInfo(EPixelFormat.PF_XGXR8,              "XGXR8",                 1,          1,          1,          4,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R8G8B8A8_UINT,      "R8G8B8A8_UINT",         1,          1,          1,          4,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R8G8B8A8_SNORM,     "R8G8B8A8_SNORM",        1,          1,          1,          4,          4,              1),

  FPixelFormatInfo(EPixelFormat.PF_R16G16B16A16_UNORM, "R16G16B16A16_UINT",     1,          1,          1,          8,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R16G16B16A16_SNORM, "R16G16B16A16_SINT",     1,          1,          1,          8,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_PLATFORM_HDR_0,     "PLATFORM_HDR_0",        0,          0,          0,          0,          0,              0),
  FPixelFormatInfo(EPixelFormat.PF_PLATFORM_HDR_1,     "PLATFORM_HDR_1",        0,          0,          0,          0,          0,              0),
  FPixelFormatInfo(EPixelFormat.PF_PLATFORM_HDR_2,     "PLATFORM_HDR_2",        0,          0,          0,          0,          0,              0),

  # NV12 contains 2 textures: R8 luminance plane followed by R8G8 1/4 size chrominance plane.
  # BlockSize/BlockBytes/NumComponents values don't make much sense for this format, so set them all to one.
  FPixelFormatInfo(EPixelFormat.PF_NV12,               "NV12",                  1,          1,          1,          1,          1,              0),

  FPixelFormatInfo(EPixelFormat.PF_R32G32_UINT,        "PF_R32G32_UINT",        1,          1,          1,          8,          2,              1),

  FPixelFormatInfo(EPixelFormat.PF_ETC2_R11_EAC,       "PF_ETC2_R11_EAC",       4,          4,          1,          8,          1,              0),
  FPixelFormatInfo(EPixelFormat.PF_ETC2_RG11_EAC,      "PF_ETC2_RG11_EAC",      4,          4,          1,          16,         2,              0),
  FPixelFormatInfo(EPixelFormat.PF_R8,                 "R8",                    1,          1,          1,          1,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_B5G5R5A1_UNORM,     "B5G5R5A1_UNORM",        1,          1,          1,          2,          4,              0),

  # ASTC HDR support
  FPixelFormatInfo(EPixelFormat.PF_ASTC_4x4_HDR,       "ASTC_4x4_HDR",          4,          4,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_6x6_HDR,       "ASTC_6x6_HDR",          6,          6,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_8x8_HDR,       "ASTC_8x8_HDR",          8,          8,          1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_10x10_HDR,     "ASTC_10x10_HDR",        10,         10,         1,          16,         4,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_12x12_HDR,     "ASTC_12x12_HDR",        12,         12,         1,          16,         4,              0),

  FPixelFormatInfo(EPixelFormat.PF_G16R16_SNORM,       "G16R16_SNORM",          1,          1,          1,          4,          2,              1),
  FPixelFormatInfo(EPixelFormat.PF_R8G8_UINT,          "R8G8_UINT",             1,          1,          1,          2,          2,              1),
  FPixelFormatInfo(EPixelFormat.PF_R32G32B32_UINT,     "R32G32B32_UINT",        1,          1,          1,          12,         3,              1),
  FPixelFormatInfo(EPixelFormat.PF_R32G32B32_SINT,     "R32G32B32_SINT",        1,          1,          1,          12,         3,              1),
  FPixelFormatInfo(EPixelFormat.PF_R32G32B32F,         "R32G32B32F",            1,          1,          1,          12,         3,              1),
  FPixelFormatInfo(EPixelFormat.PF_R8_SINT,            "R8_SINT",               1,          1,          1,          1,          1,              1),
  FPixelFormatInfo(EPixelFormat.PF_R64_UINT,           "R64_UINT",              1,          1,          1,          8,          1,              0),
  FPixelFormatInfo(EPixelFormat.PF_R9G9B9EXP5,         "R9G9B9EXP5",			      1,		      1,	    	  1,	   	    4,          4,              0),

  # P010 contains 2 textures: R16 luminance plane followed by R16G16 1/4 size chrominance plane. (upper 10 bits used)
  # BlockSize/BlockBytes/NumComponents values don't make much sense for this format, so set them all to one.
  FPixelFormatInfo(EPixelFormat.PF_P010,               "P010",				          1,          1,          1,          2,          1,              0),

  # ASTC high precision NormalRG support
  FPixelFormatInfo(EPixelFormat.PF_ASTC_4x4_NORM_RG,   "ASTC_4x4_NORM_RG",      4,          4,          1,          16,         2,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_6x6_NORM_RG,   "ASTC_6x6_NORM_RG",      6,          6,          1,          16,         2,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_8x8_NORM_RG,   "ASTC_8x8_NORM_RG",      8,          8,          1,          16,         2,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_10x10_NORM_RG, "ASTC_10x10_NORM_RG",    10,         10,         1,          16,         2,              0),
  FPixelFormatInfo(EPixelFormat.PF_ASTC_12x12_NORM_RG, "ASTC_12x12_NORM_RG",    12,         12,         1,          16,         2,              0),

  FPixelFormatInfo(EPixelFormat.PF_R16G16_SINT,        "PF_R16G16_SINT",        1,          1,          1,          4,          4,              1),
  FPixelFormatInfo(EPixelFormat.PF_R8G8B8,             "R8G8B8",                1,          1,          1,          3,          3,              0),
]
