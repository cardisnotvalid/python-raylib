import ctypes
from ctypes import (
    c_int,
    c_byte,
    c_long,
    c_float,
    c_uint,
    c_ubyte,
    c_bool,
    c_ushort,
    c_double,
    c_char_p,
    c_void_p,
)

class Color(ctypes.Structure):
    _fields_ = (
        ("r", c_ubyte),
        ("g", c_ubyte),
        ("b", c_ubyte),
        ("a", c_ubyte),
    )
    

LIGHTGRAY  = Color(200, 200, 200, 255)
GRAY       = Color(130, 130, 130, 255)
DARKGRAY   = Color(80, 80, 80, 255)
YELLOW     = Color(253, 249, 0, 255)
GOLD       = Color(255, 203, 0, 255)
ORANGE     = Color(255, 161, 0, 255)
PINK       = Color(255, 109, 194, 255)
RED        = Color(230, 41, 55, 255)
MAROON     = Color(190, 33, 55, 255)
GREEN      = Color(0, 228, 48, 255)
LIME       = Color(0, 158, 47, 255)
DARKGREEN  = Color(0, 117, 44, 255)
SKYBLUE    = Color(102, 191, 255, 255)
BLUE       = Color(0, 121, 241, 255)
DARKBLUE   = Color(0, 82, 172, 255)
PURPLE     = Color(200, 122, 255, 255)
VIOLET     = Color(135, 60, 190, 255)
DARKPURPLE = Color(112, 31, 126, 255)
BEIGE      = Color(211, 176, 131, 255)
BROWN      = Color(127, 106, 79, 255)
DARKBROWN  = Color(76, 63, 47, 255)

WHITE      = Color(255, 255, 255, 255)
BLACK      = Color(0, 0, 0, 255)
BLANK      = Color(0, 0, 0, 0)
MAGENTA    = Color(255, 0, 255, 255)
RAYWHITE   = Color(245, 245, 245, 255)


PI = 3.14159265358979323846


class Vector2(ctypes.Structure):
    _fields_ = (
        ("x", c_float),
        ("y", c_float),
    )


class Vector3(ctypes.Structure):
    _fields_ = (
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    )


class Vector4(ctypes.Structure):
    _fields_ = (
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    )


class Quaternion(Vector4):
    pass


class Matrix(ctypes.Structure):
    _fields_ = (
        ("m0", c_float),
        ("m1", c_float),
        ("m2", c_float),
        ("m3", c_float),
        ("m4", c_float),
        ("m5", c_float),
        ("m6", c_float),
        ("m7", c_float),
        ("m8", c_float),
        ("m9", c_float),
        ("m10", c_float),
        ("m11", c_float),
        ("m12", c_float),
        ("m13", c_float),
        ("m14", c_float),
        ("m15", c_float),
    )


class Rectangle(ctypes.Structure):
    _fields_ = (
        ("x", c_float),
        ("y", c_float),
        ("width", c_float),
        ("height", c_float),
    )


class Image(ctypes.Structure):
    _fields_ = (
        ("data", c_void_p),
        ("width", c_int),
        ("height", c_int),
        ("mipmaps", c_int),
        ("format", c_int),
    )


class Texture(ctypes.Structure):
    _fields_ = (
        ("id", c_uint),
        ("width", c_int),
        ("height", c_int),
        ("mipmaps", c_int),
        ("foramt", c_int),
    )


class Texture2D(Texture):
    pass


class TextureCubemap(Texture):
    pass


class RenderTexture(ctypes.Structure):
    _fields_ = (
        ("id", c_uint),
        ("texture", Texture),
        ("depth", Texture),
    )


class RenderTexture2D(RenderTexture):
    pass


class NPatchInfo(ctypes.Structure):
    _fields_ = (
        ("source", Rectangle),
        ("left", c_int),
        ("top", c_int),
        ("right", c_int),
        ("bottom", c_int),
        ("layout", c_int),
    )


class GlyphInfo(ctypes.Structure):
    _fields_ = (
        ("value", c_int),
        ("offsetX", c_int),
        ("offsetY", c_int),
        ("advanceX", c_int),
        ("image", Image),
    )


class Font(ctypes.Structure):
    _fields_ = (
        ("baseSize", c_int),
        ("glyphCount", c_int),
        ("glyphPadding", c_int),
        ("texture", Texture2D),
        ("recs", ctypes.POINTER(Rectangle)),
        ("glyphs", ctypes.POINTER(GlyphInfo)),
    )


class Camera3D(ctypes.Structure):
    _fields_ = (
        ("position", Vector3),
        ("target", Vector3),
        ("up", Vector3),
        ("fovy", c_float),
        ("projection", c_int),
    )


Camera = Camera3D


class Camera2D(ctypes.Structure):
    _fields_ = (
        ("offset", Vector2),
        ("target", Vector2),
        ("rotation", c_float),
        ("zoom", c_float),
    )


class Mesh(ctypes.Structure):
    _fields_ = (
        ("vertexCount", c_int),
        ("triangleCount", c_int),
        ("vertices", ctypes.POINTER(c_float)),
        ("texcoords", ctypes.POINTER(c_float)),
        ("texcoords2", ctypes.POINTER(c_float)),
        ("normals", ctypes.POINTER(c_float)),
        ("tangents", ctypes.POINTER(c_float)),
        ("colors", ctypes.POINTER(c_ubyte)),
        ("indices", ctypes.POINTER(c_ushort)),
        ("animVertices", ctypes.POINTER(c_float)),
        ("animNormals", ctypes.POINTER(c_float)),
        ("boneIds", ctypes.POINTER(c_ubyte)),
        ("boneWeights", ctypes.POINTER(c_float)),
        ("vaoId", ctypes.POINTER(c_uint)),
        ("vbaoId", ctypes.POINTER(c_uint)),
    )


class Shader(ctypes.Structure):
    _fields_ = (
        ("id", c_uint),
        ("locs", ctypes.POINTER(c_int)),
    )


class MaterialMap(ctypes.Structure):
    _fields_ = (
        ("texture", Texture2D),
        ("color", Color),
        ("value", c_float),
    )


class Material(ctypes.Structure):
    _fields_ = (
        ("shader", Shader),
        ("maps", ctypes.POINTER(MaterialMap)),
        ("params", c_float * 4),
    )


class Transform(ctypes.Structure):
    _fields_ = (
        ("translation", Vector3),
        ("rotation", Quaternion),
        ("scale", Vector3),
    )


class BoneInfo(ctypes.Structure):
    _fields_ = (
        ("name", c_byte * 32),
        ("parent", c_int)
    )


class Model(ctypes.Structure):
    _fields_ = (
        ("transform", Matrix),
        ("meshCount", c_int),
        ("materialCount", c_int),
        ("meshes", ctypes.POINTER(Mesh)),
        ("materials", ctypes.POINTER(Material)),
        ("meshMaterials", ctypes.POINTER(c_int)),
        ("boneCount", c_int),
        ("bones", ctypes.POINTER(BoneInfo)),
        ("bindPose", ctypes.POINTER(Transform)),
    )


class ModelAnimation(ctypes.Structure):
    _fields_ = (
        ("boneCount", c_int),
        ("frameCount", c_int),
        ("bones", ctypes.POINTER(BoneInfo)),
        ("framePoses", ctypes.POINTER(ctypes.POINTER(Transform))),
        ("name", c_byte * 32),
    )


class Ray(ctypes.Structure):
    _fields_ = (
        ("position", Vector3),
        ("direction", Vector3),
    )


class RayCollision(ctypes.Structure):
    _fields_ = (
        ("hit", c_bool),
        ("distance", c_float),
        ("point", Vector3),
        ("normal", Vector3),
    )


class BoundingBox(ctypes.Structure):
    _fields_ = (
        ("min", Vector3),
        ("max", Vector3),
    )


class Wave(ctypes.Structure):
    _fields_ = (
        ("frameCount", c_uint),
        ("sampleRate", c_uint),
        ("sampleSize", c_uint),
        ("channels", c_uint),
        ("data", ctypes.POINTER(c_void_p)),
    )


# TODO: Finish it
class rAudioBuffer(ctypes.Structure):
    pass


# TODO: Finish it
class rAudioProcessor(ctypes.Structure):
    pass


class AudioStream(ctypes.Structure):
    _fields_ = (
        ("buffer", ctypes.POINTER(rAudioBuffer)),
        ("processor", ctypes.POINTER(rAudioProcessor)),
        ("sampleRate", c_uint),
        ("sampleSize", c_uint),
        ("channels", c_uint),
    )


class Sound(ctypes.Structure):
    _fields_ = (
        ("stream", AudioStream),
        ("frameCount", c_uint),
    )


class Music(ctypes.Structure):
    _fields_ = (
        ("stream", AudioStream),
        ("frameCount", c_uint),
        ("looping", c_bool),
        ("ctxType", c_int),
        ("ctxData", ctypes.POINTER(c_void_p)),
    )


class VrDeviceInfo(ctypes.Structure):
    _fields_ = (
        ("hResolution", c_int),
        ("vResolution", c_int),
        ("hScreenSize", c_float),
        ("vScreenSize", c_float),
        ("vScreenCenter", c_float),
        ("eyeToScreenDistance", c_float),
        ("lensSeparationDistance", c_float),
        ("interpupillaryDistance", c_float),
        ("lensDistortionValues", c_float * 4),
        ("chromaAbCorrection", c_float * 4),
    )


class VrStereoConfig(ctypes.Structure):
    _fields_ = (
        ("projection", Matrix * 2),
        ("viewOffset", Matrix * 2),
        ("leftLensCenter", c_float * 2),
        ("rightLensCenter", c_float * 2),
        ("leftScreenCenter", c_float * 2),
        ("rightScreenCenter", c_float * 2),
        ("scale", c_float * 2),
        ("scaleIn", c_float * 2),
    )


class FilePathList(ctypes.Structure):
    _fields_ = (
        ("capacity", c_uint),
        ("count", c_uint),
        ("paths", ctypes.POINTER(ctypes.POINTER(c_byte))),
    )


class AutomationEvent(ctypes.Structure):
    _fields_ = (
        ("frame", c_uint),
        ("type", c_uint),
        ("params", c_int * 4),
    )


class AutomationEventList(ctypes.Structure):
    _fields_ = (
        ("capacity", c_uint),
        ("count", c_uint),
        ("events", ctypes.POINTER(AutomationEvent)),
    )


class ConfigFlags:
    FLAG_VSYNC_HINT         = 0x00000040
    FLAG_FULLSCREEN_MODE    = 0x00000002
    FLAG_WINDOW_RESIZABLE   = 0x00000004
    FLAG_WINDOW_UNDECORATED = 0x00000008
    FLAG_WINDOW_HIDDEN      = 0x00000080
    FLAG_WINDOW_MINIMIZED   = 0x00000200
    FLAG_WINDOW_MAXIMIZED   = 0x00000400
    FLAG_WINDOW_UNFOCUSED   = 0x00000800
    FLAG_WINDOW_TOPMOST     = 0x00001000
    FLAG_WINDOW_ALWAYS_RUN  = 0x00000100
    FLAG_WINDOW_TRANSPARENT = 0x00000010
    FLAG_WINDOW_HIGHDPI     = 0x00002000
    FLAG_WINDOW_MOUSE_PASSTHROUGH = 0x00004000
    FLAG_BORDERLESS_WINDOWED_MODE = 0x00008000
    FLAG_MSAA_4X_HINT       = 0x00000020
    FLAG_INTERLACED_HINT    = 0x00010000


class TraceLogLevel:
    LOG_ALL     = 0
    LOG_TRACE   = 1
    LOG_DEBUG   = 2
    LOG_INFO    = 3
    LOG_WARNING = 4
    LOG_ERROR   = 5
    LOG_FATAL   = 6
    LOG_NONE    = 7


class KeyboardKey:
    KEY_NULL            = 0
    # Alphanumeric keys
    KEY_APOSTROPHE      = 39
    KEY_COMMA           = 44
    KEY_MINUS           = 45
    KEY_PERIOD          = 46
    KEY_SLASH           = 47
    KEY_ZERO            = 48
    KEY_ONE             = 49
    KEY_TWO             = 50
    KEY_THREE           = 51
    KEY_FOUR            = 52
    KEY_FIVE            = 53
    KEY_SIX             = 54
    KEY_SEVEN           = 55
    KEY_EIGHT           = 56
    KEY_NINE            = 57
    KEY_SEMICOLON       = 59
    KEY_EQUAL           = 61
    KEY_A               = 65
    KEY_B               = 66
    KEY_C               = 67
    KEY_D               = 68
    KEY_E               = 69
    KEY_F               = 70
    KEY_G               = 71
    KEY_H               = 72
    KEY_I               = 73
    KEY_J               = 74
    KEY_K               = 75
    KEY_L               = 76
    KEY_M               = 77
    KEY_N               = 78
    KEY_O               = 79
    KEY_P               = 80
    KEY_Q               = 81
    KEY_R               = 82
    KEY_S               = 83
    KEY_T               = 84
    KEY_U               = 85
    KEY_V               = 86
    KEY_W               = 87
    KEY_X               = 88
    KEY_Y               = 89
    KEY_Z               = 90
    KEY_LEFT_BRACKET    = 91
    KEY_BACKSLASH       = 92
    KEY_RIGHT_BRACKET   = 93
    KEY_GRAVE           = 96
    # Function keys
    KEY_SPACE           = 32
    KEY_ESCAPE          = 256
    KEY_ENTER           = 257
    KEY_TAB             = 258
    KEY_BACKSPACE       = 259
    KEY_INSERT          = 260
    KEY_DELETE          = 261
    KEY_RIGHT           = 262
    KEY_LEFT            = 263
    KEY_DOWN            = 264
    KEY_UP              = 265
    KEY_PAGE_UP         = 266
    KEY_PAGE_DOWN       = 267
    KEY_HOME            = 268
    KEY_END             = 269
    KEY_CAPS_LOCK       = 280
    KEY_SCROLL_LOCK     = 281
    KEY_NUM_LOCK        = 282
    KEY_PRINT_SCREEN    = 283
    KEY_PAUSE           = 284
    KEY_F1              = 290
    KEY_F2              = 291
    KEY_F3              = 292
    KEY_F4              = 293
    KEY_F5              = 294
    KEY_F6              = 295
    KEY_F7              = 296
    KEY_F8              = 297
    KEY_F9              = 298
    KEY_F10             = 299
    KEY_F11             = 300
    KEY_F12             = 301
    KEY_LEFT_SHIFT      = 340
    KEY_LEFT_CONTROL    = 341
    KEY_LEFT_ALT        = 342
    KEY_LEFT_SUPER      = 343
    KEY_RIGHT_SHIFT     = 344
    KEY_RIGHT_CONTROL   = 345
    KEY_RIGHT_ALT       = 346
    KEY_RIGHT_SUPER     = 347
    KEY_KB_MENU         = 348
    # Keypad keys
    KEY_KP_0            = 320
    KEY_KP_1            = 321
    KEY_KP_2            = 322
    KEY_KP_3            = 323
    KEY_KP_4            = 324
    KEY_KP_5            = 325
    KEY_KP_6            = 326
    KEY_KP_7            = 327
    KEY_KP_8            = 328
    KEY_KP_9            = 329
    KEY_KP_DECIMAL      = 330
    KEY_KP_DIVIDE       = 331
    KEY_KP_MULTIPLY     = 332
    KEY_KP_SUBTRACT     = 333
    KEY_KP_ADD          = 334
    KEY_KP_ENTER        = 335
    KEY_KP_EQUAL        = 336
    # Android key buttons
    KEY_BACK            = 4
    KEY_MENU            = 82
    KEY_VOLUME_UP       = 24
    KEY_VOLUME_DOWN     = 25


class MouseButton:
    MOUSE_BUTTON_LEFT    = 0
    MOUSE_BUTTON_RIGHT   = 1
    MOUSE_BUTTON_MIDDLE  = 2
    MOUSE_BUTTON_SIDE    = 3
    MOUSE_BUTTON_EXTRA   = 4
    MOUSE_BUTTON_FORWARD = 5
    MOUSE_BUTTON_BACK    = 6


class MouseCursor:
    MOUSE_CURSOR_DEFAULT       = 0
    MOUSE_CURSOR_ARROW         = 1
    MOUSE_CURSOR_IBEAM         = 2
    MOUSE_CURSOR_CROSSHAIR     = 3
    MOUSE_CURSOR_POINTING_HAND = 4
    MOUSE_CURSOR_RESIZE_EW     = 5
    MOUSE_CURSOR_RESIZE_NS     = 6
    MOUSE_CURSOR_RESIZE_NWSE   = 7
    MOUSE_CURSOR_RESIZE_NESW   = 8
    MOUSE_CURSOR_RESIZE_ALL    = 9
    MOUSE_CURSOR_NOT_ALLOWED   = 10


class GamepadButton:
    GAMEPAD_BUTTON_UNKNOWN          = 0
    GAMEPAD_BUTTON_LEFT_FACE_UP     = 1
    GAMEPAD_BUTTON_LEFT_FACE_RIGHT  = 2
    GAMEPAD_BUTTON_LEFT_FACE_DOWN   = 3
    GAMEPAD_BUTTON_LEFT_FACE_LEFT   = 4
    GAMEPAD_BUTTON_RIGHT_FACE_UP    = 5
    GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = 6
    GAMEPAD_BUTTON_RIGHT_FACE_DOWN  = 7
    GAMEPAD_BUTTON_RIGHT_FACE_LEFT  = 8
    GAMEPAD_BUTTON_LEFT_TRIGGER_1   = 9
    GAMEPAD_BUTTON_LEFT_TRIGGER_2   = 10
    GAMEPAD_BUTTON_RIGHT_TRIGGER_1  = 11
    GAMEPAD_BUTTON_RIGHT_TRIGGER_2  = 12
    GAMEPAD_BUTTON_MIDDLE_LEFT      = 13
    GAMEPAD_BUTTON_MIDDLE           = 14
    GAMEPAD_BUTTON_MIDDLE_RIGHT     = 15
    GAMEPAD_BUTTON_LEFT_THUMB       = 16
    GAMEPAD_BUTTON_RIGHT_THUMB      = 17


class GamepadAxis:
    GAMEPAD_AXIS_LEFT_X        = 0
    GAMEPAD_AXIS_LEFT_Y        = 1
    GAMEPAD_AXIS_RIGHT_X       = 2
    GAMEPAD_AXIS_RIGHT_Y       = 3
    GAMEPAD_AXIS_LEFT_TRIGGER  = 4
    GAMEPAD_AXIS_RIGHT_TRIGGER = 5


class MaterialMapIndex:
    MATERIAL_MAP_ALBEDO     = 0
    MATERIAL_MAP_METALNESS  = 1
    MATERIAL_MAP_NORMAL     = 2
    MATERIAL_MAP_ROUGHNESS  = 3
    MATERIAL_MAP_OCCLUSION  = 4
    MATERIAL_MAP_EMISSION   = 5
    MATERIAL_MAP_HEIGHT     = 6
    MATERIAL_MAP_CUBEMAP    = 7
    MATERIAL_MAP_IRRADIANCE = 8
    MATERIAL_MAP_PREFILTER  = 9
    MATERIAL_MAP_BRDF       = 10


class ShaderLocationIndex:
    SHADER_LOC_VERTEX_POSITION   = 0
    SHADER_LOC_VERTEX_TEXCOORD01 = 1
    SHADER_LOC_VERTEX_TEXCOORD02 = 2
    SHADER_LOC_VERTEX_NORMAL     = 3
    SHADER_LOC_VERTEX_TANGENT    = 4
    SHADER_LOC_VERTEX_COLOR      = 5
    SHADER_LOC_MATRIX_MVP        = 6
    SHADER_LOC_MATRIX_VIEW       = 7
    SHADER_LOC_MATRIX_PROJECTION = 8
    SHADER_LOC_MATRIX_MODEL      = 9
    SHADER_LOC_MATRIX_NORMAL     = 10
    SHADER_LOC_VECTOR_VIEW       = 11
    SHADER_LOC_COLOR_DIFFUSE     = 12
    SHADER_LOC_COLOR_SPECULAR    = 12
    SHADER_LOC_COLOR_AMBIENT     = 13
    SHADER_LOC_MAP_ALBEDO        = 13
    SHADER_LOC_MAP_METALNESS     = 14
    SHADER_LOC_MAP_NORMAL        = 15
    SHADER_LOC_MAP_ROUGHNESS     = 16
    SHADER_LOC_MAP_OCCLUSION     = 17
    SHADER_LOC_MAP_EMISSION      = 18
    SHADER_LOC_MAP_HEIGHT        = 19
    SHADER_LOC_MAP_CUBEMAP       = 20
    SHADER_LOC_MAP_IRRADIANCE    = 21
    SHADER_LOC_MAP_PREFILTER     = 22
    SHADER_LOC_MAP_BRDF          = 23


class ShaderUniformDataType:
    SHADER_UNIFORM_FLOAT     = 0
    SHADER_UNIFORM_VEC2      = 1
    SHADER_UNIFORM_VEC3      = 2
    SHADER_UNIFORM_VEC4      = 3
    SHADER_UNIFORM_INT       = 4
    SHADER_UNIFORM_IVEC2     = 5
    SHADER_UNIFORM_IVEC3     = 6
    SHADER_UNIFORM_IVEC4     = 7
    SHADER_UNIFORM_SAMPLER2D = 8


class ShaderAttributeDataType:
    SHADER_ATTRIB_FLOAT = 0
    SHADER_ATTRIB_VEC2  = 1
    SHADER_ATTRIB_VEC3  = 2
    SHADER_ATTRIB_VEC4  = 3


class PixelFormat:
    PIXELFORMAT_UNCOMPRESSED_GRAYSCALE    = 1
    PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA   = 2
    PIXELFORMAT_UNCOMPRESSED_R5G6B5       = 3
    PIXELFORMAT_UNCOMPRESSED_R8G8B8       = 4
    PIXELFORMAT_UNCOMPRESSED_R5G5B5A1     = 5
    PIXELFORMAT_UNCOMPRESSED_R4G4B4A4     = 6
    PIXELFORMAT_UNCOMPRESSED_R8G8B8A8     = 7
    PIXELFORMAT_UNCOMPRESSED_R32          = 8
    PIXELFORMAT_UNCOMPRESSED_R32G32B32    = 9
    PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10
    PIXELFORMAT_UNCOMPRESSED_R16          = 11
    PIXELFORMAT_UNCOMPRESSED_R16G16B16    = 12
    PIXELFORMAT_UNCOMPRESSED_R16G16B16A16 = 13
    PIXELFORMAT_COMPRESSED_DXT1_RGB       = 14
    PIXELFORMAT_COMPRESSED_DXT1_RGBA      = 15
    PIXELFORMAT_COMPRESSED_DXT3_RGBA      = 16
    PIXELFORMAT_COMPRESSED_DXT5_RGBA      = 17
    PIXELFORMAT_COMPRESSED_ETC1_RGB       = 18
    PIXELFORMAT_COMPRESSED_ETC2_RGB       = 19
    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA  = 20
    PIXELFORMAT_COMPRESSED_PVRT_RGB       = 21
    PIXELFORMAT_COMPRESSED_PVRT_RGBA      = 22
    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA  = 23
    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA  = 24


class TextureFilter:
    TEXTURE_FILTER_POINT           = 0
    TEXTURE_FILTER_BILINEAR        = 1
    TEXTURE_FILTER_TRILINEAR       = 2
    TEXTURE_FILTER_ANISOTROPIC_4X  = 3
    TEXTURE_FILTER_ANISOTROPIC_8X  = 4
    TEXTURE_FILTER_ANISOTROPIC_16X = 5


class TextureWrap:
    TEXTURE_WRAP_REPEAT        = 0
    TEXTURE_WRAP_CLAMP         = 1
    TEXTURE_WRAP_MIRROR_REPEAT = 2
    TEXTURE_WRAP_MIRROR_CLAMP  = 3


class CubemapLayout:
    CUBEMAP_LAYOUT_AUTO_DETECT         = 0
    CUBEMAP_LAYOUT_LINE_VERTICAL       = 1
    CUBEMAP_LAYOUT_LINE_HORIZONTAL     = 2
    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3
    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4
    CUBEMAP_LAYOUT_PANORAMA            = 5


class FontType:
    FONT_DEFAULT = 0
    FONT_BITMAP  = 1
    FONT_SDF     = 2


class BlendMode:
    BLEND_ALPHA             = 0
    BLEND_ADDITIVE          = 1
    BLEND_MULTIPLIED        = 2
    BLEND_ADD_COLORS        = 3
    BLEND_SUBTRACT_COLORS   = 4
    BLEND_ALPHA_PREMULTIPLY = 5
    BLEND_CUSTOM            = 6
    BLEND_CUSTOM_SEPARATE   = 7


class Gesture:
    GESTURE_NONE        = 0
    GESTURE_TAP         = 1
    GESTURE_DOUBLETAP   = 2
    GESTURE_HOLD        = 4
    GESTURE_DRAG        = 8
    GESTURE_SWIPE_RIGHT = 16
    GESTURE_SWIPE_LEFT  = 32
    GESTURE_SWIPE_UP    = 64
    GESTURE_SWIPE_DOWN  = 128
    GESTURE_PINCH_IN    = 256
    GESTURE_PINCH_OUT   = 512


class CameraMode:
    CAMERA_CUSTOM       = 0
    CAMERA_FREE         = 1
    CAMERA_ORBITAL      = 2
    CAMERA_FIRST_PERSON = 3
    CAMERA_THIRD_PERSON = 4


class CameraProjection:
    CAMERA_PERSPECTIVE  = 0
    CAMERA_ORTHOGRAPHIC = 1


class NPatchLayout:
    NPATCH_NINE_PATCH             = 0
    NPATCH_THREE_PATCH_VERTICAL   = 1
    NPATCH_THREE_PATCH_HORIZONTAL = 2


raylib_dll = ctypes.CDLL("./raylib.dll")


trace_log_callback = ctypes.CFUNCTYPE(None, c_int, c_char_p, c_char_p)
load_file_data_callback = ctypes.CFUNCTYPE(ctypes.POINTER(c_ubyte), c_char_p, ctypes.POINTER(c_int))
save_file_data_callback = ctypes.CFUNCTYPE(c_bool, c_char_p, c_void_p, c_int)
load_file_text_callback = ctypes.CFUNCTYPE(c_char_p, c_char_p)
save_file_text_callback = ctypes.CFUNCTYPE(c_bool, c_char_p, c_char_p)

# Window-related functions
init_window = raylib_dll.InitWindow
init_window.argtypes = (c_int, c_int, c_char_p)
init_window.restype = None

close_window = raylib_dll.CloseWindow
close_window.argtypes = None
close_window.restype = None

window_should_close = raylib_dll.WindowShouldClose
window_should_close.argtypes = None
window_should_close.restype = c_bool

is_window_ready = raylib_dll.IsWindowReady
is_window_ready.argtypes = None
is_window_ready.restype = c_bool

is_window_fullscreen = raylib_dll.IsWindowFullscreen
is_window_fullscreen.argtypes = None
is_window_fullscreen.restype = c_bool

is_window_hidden = raylib_dll.IsWindowHidden
is_window_hidden.argtypes = None
is_window_hidden.restype = c_bool

is_window_minimized = raylib_dll.IsWindowMinimized
is_window_minimized.argtypes = None
is_window_minimized.restype = c_bool

is_window_maximized = raylib_dll.IsWindowMaximized
is_window_maximized.argtypes = None
is_window_maximized.restype = c_bool

is_window_focused = raylib_dll.IsWindowFocused
is_window_focused.argtypes = None
is_window_focused.restype = c_bool

is_window_resized = raylib_dll.IsWindowResized
is_window_resized.argtypes = None
is_window_resized.restype = c_bool

is_window_state = raylib_dll.IsWindowState
is_window_state.argtypes = (c_uint,)
is_window_state.restype = c_bool

set_window_state = raylib_dll.SetWindowState
set_window_state.argtypes = (c_uint,)
set_window_state.restype = None

clear_window_state = raylib_dll.ClearWindowState
clear_window_state.argtypes = (c_uint,)
clear_window_state.restype = None

toggle_fullscreen = raylib_dll.ToggleFullscreen
toggle_fullscreen.argtypes = None
toggle_fullscreen.restype = None

toggle_borderless_windowed = raylib_dll.ToggleBorderlessWindowed
toggle_borderless_windowed.argtypes = None
toggle_borderless_windowed.restype = None

maximize_window = raylib_dll.MaximizeWindow
maximize_window.argtypes = None
maximize_window.restype = None

minimize_window = raylib_dll.MinimizeWindow
minimize_window.argtypes = None
minimize_window.restype = None

restore_window = raylib_dll.RestoreWindow
restore_window.argtypes = None
restore_window.restype = None

set_window_icon = raylib_dll.SetWindowIcon
set_window_icon.argtypes = (Image,)
set_window_icon.restype = None

set_window_icons = raylib_dll.SetWindowIcons
set_window_icons.argtypes = (ctypes.POINTER(Image), c_int)
set_window_icons.restype = None

set_window_title = raylib_dll.SetWindowTitle
set_window_title.argtypes = (c_char_p,)
set_window_title.restype = None

set_window_position = raylib_dll.SetWindowPosition
set_window_position.argtypes = (c_int, c_int)
set_window_position.restype = None

set_window_monitor = raylib_dll.SetWindowMonitor
set_window_monitor.argtypes = (c_int,)
set_window_monitor.restype = None

set_window_min_size = raylib_dll.SetWindowMinSize
set_window_min_size.argtypes = (c_int, c_int)
set_window_min_size.restype = None

set_window_max_size = raylib_dll.SetWindowMaxSize
set_window_max_size.argtypes = (c_int, c_int)
set_window_max_size.restype = None

set_window_size = raylib_dll.SetWindowSize
set_window_size.argtypes = (c_int, c_int)
set_window_size.restype = None

set_window_opacity = raylib_dll.SetWindowOpacity
set_window_opacity.argtypes = (c_float,)
set_window_opacity.restype = None

set_window_focused = raylib_dll.SetWindowFocused
set_window_focused.restype = None

get_window_handle = raylib_dll.GetWindowHandle
get_window_handle.argtypes = None
get_window_handle.restype = c_void_p

get_screen_width = raylib_dll.GetScreenWidth
get_screen_width.argtypes = None
get_screen_width.restype = c_int

get_screen_height = raylib_dll.GetScreenHeight
get_screen_height.argtypes = None
get_screen_height.restype = c_int

get_render_width = raylib_dll.GetRenderWidth
get_render_width.argtypes = None
get_render_width.restype = c_int

get_render_height = raylib_dll.GetRenderHeight
get_render_height.argtypes = None
get_render_height.restype = c_int

get_monitor_count = raylib_dll.GetMonitorCount
get_monitor_count.argtypes = None
get_monitor_count.restype = c_int

get_current_monitor = raylib_dll.GetCurrentMonitor
get_current_monitor.argtypes = None
get_current_monitor.restype = c_int

get_monitor_position = raylib_dll.GetMonitorPosition
get_monitor_position.argtypes = (c_int,)
get_monitor_position.restype = Vector2

get_monitor_width = raylib_dll.GetMonitorWidth
get_monitor_width.argtypes = (c_int,)
get_monitor_width.restype = c_int

get_monitor_height = raylib_dll.GetMonitorHeight
get_monitor_height.argtypes = (c_int,)
get_monitor_height.restype = c_int

get_monitor_physical_width = raylib_dll.GetMonitorPhysicalWidth
get_monitor_physical_width.argtypes = (c_int,)
get_monitor_physical_width.restype = c_int

get_monitor_physical_height = raylib_dll.GetMonitorPhysicalHeight
get_monitor_physical_height.argtypes = (c_int,)
get_monitor_physical_height.restype = c_int

get_monitor_refresh_rate = raylib_dll.GetMonitorRefreshRate
get_monitor_refresh_rate.argtypes = (c_int,)
get_monitor_refresh_rate.restype = c_int

get_window_position = raylib_dll.GetWindowPosition
get_window_position.argtypes = None
get_window_position.restype = Vector2

get_window_scale_dpi = raylib_dll.GetWindowScaleDPI
get_window_scale_dpi.argtypes = None
get_window_scale_dpi.restype = Vector2

get_monitor_name = raylib_dll.GetMonitorName
get_monitor_name.argtypes = (c_int,)
get_monitor_name.restype = c_char_p

set_clipboard_text = raylib_dll.SetClipboardText
set_clipboard_text.argtypes = (c_char_p,)
set_clipboard_text.restype = None

get_clipboard_text = raylib_dll.GetClipboardText
get_clipboard_text.argtypes = None
get_clipboard_text.restype = c_char_p

enable_event_waiting = raylib_dll.EnableEventWaiting
enable_event_waiting.argtypes = None
enable_event_waiting.restype = None

disable_event_waiting = raylib_dll.DisableEventWaiting
disable_event_waiting.argtypes = None
disable_event_waiting.restype = None

# Cursor-related functions
show_cursor = raylib_dll.ShowCursor
show_cursor.argtypes = None
show_cursor.restype = None

hide_cursor = raylib_dll.HideCursor
hide_cursor.argtypes = None
hide_cursor.restype = None

is_cursor_hidden = raylib_dll.IsCursorHidden
is_cursor_hidden.argtypes = None
is_cursor_hidden.restype = c_bool

enable_cursor = raylib_dll.EnableCursor
enable_cursor.argtypes = None
enable_cursor.restype = None

disable_cursor = raylib_dll.DisableCursor
disable_cursor.argtypes = None
disable_cursor.restype = None

is_cursor_on_screen = raylib_dll.IsCursorOnScreen
is_cursor_on_screen.argtypes = None
is_cursor_on_screen.restype = c_bool

# Drawing-related functions
clear_background = raylib_dll.ClearBackground
clear_background.argtypes = (Color,)
clear_background.restype = None

begin_drawing = raylib_dll.BeginDrawing
begin_drawing.argtypes = None
begin_drawing.restype = None

end_drawing = raylib_dll.EndDrawing
end_drawing.argtypes = None
end_drawing.restype = None

begin_mode_2d = raylib_dll.BeginMode2D
begin_mode_2d.argtypes = (Camera2D,)
begin_mode_2d.restype = None

end_mode_2d = raylib_dll.EndMode2D
end_mode_2d.argtypes = None
end_mode_2d.restype = None

begin_mode_3d = raylib_dll.BeginMode3D
begin_mode_3d.argtypes = (Camera3D,)
begin_mode_3d.restype = None

end_mode_3d = raylib_dll.EndMode3D
end_mode_3d.argtypes = None
end_mode_3d.restype = None

begin_texture_mode = raylib_dll.BeginTextureMode
begin_texture_mode.argtypes = (RenderTexture2D,)
begin_texture_mode.restype = None

end_texture_mode = raylib_dll.EndTextureMode
end_texture_mode.argtypes = None
end_texture_mode.restype = None

begin_shader_mode = raylib_dll.BeginShaderMode
begin_shader_mode.argtypes = (Shader,)
begin_shader_mode.restype = None

end_shader_mode = raylib_dll.EndShaderMode
end_shader_mode.argtypes = None
end_shader_mode.restype = None

begin_blend_mode = raylib_dll.BeginBlendMode
begin_blend_mode.argtypes = (c_int,)
begin_blend_mode.restype = None

end_blend_mode = raylib_dll.EndBlendMode
end_blend_mode.argtypes = None
end_blend_mode.restype = None

begin_scissor_mode = raylib_dll.BeginScissorMode
begin_scissor_mode.argtypes = (c_int, c_int, c_int, c_int)
begin_scissor_mode.restype = None

end_scissor_mode = raylib_dll.EndScissorMode
end_scissor_mode.argtypes = None
end_scissor_mode.restype = None

begin_vr_stereo_mode = raylib_dll.BeginVrStereoMode
begin_vr_stereo_mode.argtypes = (VrStereoConfig,)
begin_vr_stereo_mode.restype = None

end_vr_stereo_mode = raylib_dll.EndVrStereoMode
end_vr_stereo_mode.argtypes = None
end_vr_stereo_mode.restype = None

# VR stereo config functions for VR simulator
load_vr_stereo_config = raylib_dll.LoadVrStereoConfig
load_vr_stereo_config.argtypes = (VrDeviceInfo,)
load_vr_stereo_config.restype = VrStereoConfig

# Shader management functions
load_shader = raylib_dll.LoadShader
load_shader.argtypes = (c_char_p, c_char_p)
load_shader.restype = Shader

load_shader_from_memory = raylib_dll.LoadShaderFromMemory
load_shader_from_memory.argtypes = (c_char_p, c_char_p)
load_shader_from_memory.restype = Shader

is_shader_ready = raylib_dll.IsShaderReady
is_shader_ready.argtypes = (Shader,)
is_shader_ready.restype = c_bool

get_shader_location = raylib_dll.GetShaderLocation
get_shader_location.argtypes = (Shader, c_char_p)
get_shader_location.restype = c_int

get_shader_location_attrib = raylib_dll.GetShaderLocationAttrib
get_shader_location_attrib.argtypes = (Shader, c_char_p)
get_shader_location_attrib.restype = c_int

set_shader_value = raylib_dll.SetShaderValue
set_shader_value.argtypes = (Shader, c_int, c_void_p, c_int)
set_shader_value.restype = None

set_shader_value_v = raylib_dll.SetShaderValueV
set_shader_value_v.argtypes = (Shader, c_int, c_void_p, c_int, c_int)
set_shader_value_v.restype = None

set_shader_value_matrix = raylib_dll.SetShaderValueMatrix
set_shader_value_matrix.argtypes = (Shader, c_int, Matrix)
set_shader_value_matrix.restype = None

set_shader_value_texture = raylib_dll.SetShaderValueTexture
set_shader_value_texture.argtypes = (Shader, c_int, Texture2D)
set_shader_value_texture.restype = None

unload_shader = raylib_dll.UnloadShader
unload_shader.argtypes = (Shader,)
unload_shader.restype = None

# Screen-space-related functions
get_mouse_ray = raylib_dll.GetMouseRay
get_mouse_ray.argtypes = (Vector2, Camera)
get_mouse_ray.restype = Ray

get_camera_matrix = raylib_dll.GetCameraMatrix
get_camera_matrix.argtypes = (Camera,)
get_camera_matrix.restype = Matrix

get_camera_matrix_2d = raylib_dll.GetCameraMatrix2D
get_camera_matrix_2d.argtypes = (Camera2D,)
get_camera_matrix_2d.restype = Matrix

get_world_to_screen = raylib_dll.GetWorldToScreen
get_world_to_screen.argtypes = (Vector3, Camera)
get_world_to_screen.restype = Vector2

get_screen_to_world_2d = raylib_dll.GetScreenToWorld2D
get_screen_to_world_2d.argtypes = (Vector2, Camera2D)
get_screen_to_world_2d.restype = Vector2

get_world_to_screen_ex = raylib_dll.GetWorldToScreenEx
get_world_to_screen_ex.argtypes = (Vector3, Camera, c_int, c_int)
get_world_to_screen_ex.restype = Vector2

get_world_to_screen_2d = raylib_dll.GetScreenToWorld2D
get_world_to_screen_2d.argtypes = (Vector2, Camera2D)
get_world_to_screen_2d.restype = Vector2

# Timing-related functions
set_target_fps = raylib_dll.SetTargetFPS
set_target_fps.argtypes = (c_int,)
set_target_fps.restype = None

get_frame_time = raylib_dll.GetFrameTime
get_frame_time.argtypes = None
get_frame_time.restype = c_float

get_time = raylib_dll.GetTime
get_time.argtypes = None
get_time.restype = c_double

get_fps = raylib_dll.GetFPS
get_fps.argtypes = None
get_fps.restype = c_int

# Custom frame control functions
swap_screen_buffer = raylib_dll.SwapScreenBuffer
swap_screen_buffer.argtypes = None
swap_screen_buffer.restype = None

poll_input_events = raylib_dll.PollInputEvents
poll_input_events.argtypes = None
poll_input_events.restype = None

wait_time = raylib_dll.WaitTime
wait_time.argtypes = (c_double,)
wait_time.restype = None

set_random_seed = raylib_dll.SetRandomSeed
set_random_seed.argtypes = (c_uint,)
set_random_seed.restype = None

get_random_value = raylib_dll.GetRandomValue
get_random_value.argtypes = (c_int, c_int)
get_random_value.restype = c_int

load_random_sequence = raylib_dll.LoadRandomSequence
load_random_sequence.argtypes = (c_uint, c_int, c_int)
load_random_sequence.restype = ctypes.POINTER(c_int)

unload_random_sequence = raylib_dll.UnloadRandomSequence
unload_random_sequence.argtypes = (ctypes.POINTER(c_int),)
unload_random_sequence.restype = None

# Misc. functions
take_screenshot = raylib_dll.TakeScreenshot
take_screenshot.argtypes = (c_char_p,)
take_screenshot.restype = None

set_config_flags = raylib_dll.SetConfigFlags
set_config_flags.argtypes = (c_uint,)
set_config_flags.restype = None

open_url = raylib_dll.OpenURL
open_url.argtypes = (c_char_p,)
open_url.restype = None

trace_log = raylib_dll.TraceLog
trace_log.argtypes = (c_int, c_char_p)
trace_log.restype = None

set_trace_log_level = raylib_dll.SetTraceLogLevel
set_trace_log_level.argtypes = (c_int,)
set_trace_log_level.restype = None

mem_alloc = raylib_dll.MemAlloc
mem_alloc.argtypes = (c_uint,)
mem_alloc.restype = c_void_p

mem_realloc = raylib_dll.MemRealloc
mem_realloc.argtypes = (c_void_p, c_uint)
mem_realloc.restype = c_void_p

mem_free = raylib_dll.MemFree
mem_free.argtypes = (c_void_p,)
mem_free.restype = None

# Set custom callbacks
set_trace_log_callback = raylib_dll.SetTraceLogCallback
set_trace_log_callback.argtypes = (trace_log_callback,)
set_trace_log_callback.restype = None

set_load_file_data_callback = raylib_dll.SetLoadFileDataCallback
set_load_file_data_callback.argtypes = (load_file_data_callback,)
set_load_file_data_callback.restype = None

set_save_file_data_callback = raylib_dll.SetSaveFileTextCallback
set_save_file_data_callback.argtypes = (save_file_data_callback,)
set_save_file_data_callback.restype = None

set_load_file_text_callback = raylib_dll.SetLoadFileTextCallback
set_load_file_text_callback.argtypes = (load_file_text_callback,)
set_load_file_text_callback.restype = None

set_save_file_text_callback = raylib_dll.SetSaveFileTextCallback
set_save_file_text_callback.argtypes = (save_file_text_callback,)
set_save_file_text_callback.restype = None

# Files management functions
load_file_data = raylib_dll.LoadFileData
load_file_data.argtypes = (c_char_p, c_int)
load_file_data.restype = c_char_p

unload_file_data = raylib_dll.UnloadFileData
unload_file_data.argtypes = (c_char_p,)
unload_file_data.restype = None

save_file_data = raylib_dll.SaveFileData
save_file_data.argtypes = (c_char_p, c_void_p, c_int)
save_file_data.restype = c_bool

export_data_as_code = raylib_dll.ExportDataAsCode
export_data_as_code.argtypes = (ctypes.POINTER(c_ubyte), c_int, c_char_p)
export_data_as_code.restype = c_bool

load_file_text = raylib_dll.LoadFileText
load_file_text.argtypes = (c_char_p,)
load_file_text.restype = c_char_p

unload_file_text = raylib_dll.UnloadFileText
unload_file_text.argtypes = (c_char_p,)
unload_file_text.restype = None

save_file_text = raylib_dll.SaveFileText
save_file_text.argtypes = (c_char_p, c_char_p)
save_file_text.restype = c_bool

# File system functions
file_exists = raylib_dll.FileExists
file_exists.argtypes = (c_char_p,)
file_exists.restype = c_bool

directory_exists = raylib_dll.DirectoryExists
directory_exists.argtypes = (c_char_p,)
directory_exists.restype = c_bool

is_file_extension = raylib_dll.IsFileExtension
is_file_extension.argtypes = (c_char_p, c_char_p)
is_file_extension.restype = c_bool

get_file_length = raylib_dll.GetFileLength
get_file_length.argtypes = (c_char_p,)
get_file_length.restype = c_int

get_file_extension = raylib_dll.GetFileExtension
get_file_extension.argtypes = (c_char_p,)
get_file_extension.restype = c_char_p

get_file_name = raylib_dll.GetFileName
get_file_name.argtypes = (c_char_p,)
get_file_name.restype = c_char_p

get_file_name_without_ext = raylib_dll.GetFileNameWithoutExt
get_file_name_without_ext.argtypes = (c_char_p,)
get_file_name_without_ext.restype = c_char_p

get_directory_path = raylib_dll.GetDirectoryPath
get_directory_path.argtypes = (c_char_p,)
get_directory_path.restype = c_char_p

get_prev_directory_path = raylib_dll.GetPrevDirectoryPath
get_prev_directory_path.argtypes = (c_char_p,)
get_prev_directory_path.restype = c_char_p

get_working_directory = raylib_dll.GetWorkingDirectory
get_working_directory.argtypes = None
get_working_directory.restype = c_char_p

get_application_directory = raylib_dll.GetApplicationDirectory
get_application_directory.argtypes = None
get_application_directory.restype = c_char_p

change_directory = raylib_dll.ChangeDirectory
change_directory.argtypes = (c_char_p,)
change_directory.restype = c_bool

is_path_file = raylib_dll.IsPathFile
is_path_file.argtypes = (c_char_p,)
is_path_file.restype = c_bool

load_directory_files = raylib_dll.LoadDirectoryFiles
load_directory_files.argtypes = (c_char_p,)
load_directory_files.restype = FilePathList

load_directory_files_ex = raylib_dll.LoadDirectoryFilesEx
load_directory_files_ex.argtypes = (c_char_p, c_char_p, c_bool)
load_directory_files_ex.restype = FilePathList

unload_directory_files = raylib_dll.UnloadDirectoryFiles
unload_directory_files.argtypes = (FilePathList,)
unload_directory_files.restype = None

is_file_dropped = raylib_dll.IsFileDropped
is_file_dropped.argtypes = None
is_file_dropped.restype = c_bool

load_dropped_files = raylib_dll.LoadDroppedFiles
load_dropped_files.argtypes = None
load_dropped_files.restype = FilePathList

unload_dropped_files = raylib_dll.UnloadDroppedFiles
unload_dropped_files.argtypes = (FilePathList,)
unload_dropped_files.restype = None

get_file_mode_time = raylib_dll.GetFileModTime
get_file_mode_time.argtypes = (c_char_p,)
get_file_mode_time.restype = c_long

# Compression/Encoding functionality
compress_data = raylib_dll.CompressData
compress_data.argtypes = (ctypes.POINTER(c_uint), c_int, c_int)
compress_data.restype = ctypes.POINTER(c_uint)

decompress_data = raylib_dll.DecompressData
decompress_data.argtypes = (ctypes.POINTER(c_uint), c_int, c_int)
decompress_data.restype = ctypes.POINTER(c_uint)

encode_data_base64 = raylib_dll.EncodeDataBase64
encode_data_base64.argtypes = (ctypes.POINTER(c_uint), c_int, c_int)
encode_data_base64.restype = c_char_p

decode_data_base64 = raylib_dll.DecodeDataBase64
decode_data_base64.argtypes = (ctypes.POINTER(c_uint), c_char_p, ctypes.POINTER(c_int))
decode_data_base64.restype = ctypes.POINTER(c_uint)

# Automation events functionality
load_automation_event_list = raylib_dll.LoadAutomationEventList
load_automation_event_list.argtypes = (c_char_p,)
load_automation_event_list.restype = AutomationEventList

unload_automation_event_list = raylib_dll.UnloadAutomationEventList
unload_automation_event_list.argtypes = (ctypes.POINTER(AutomationEventList),)
unload_automation_event_list.restype = None

export_automation_event_list = raylib_dll.ExportAutomationEventList
export_automation_event_list.argtypes = (AutomationEventList, c_char_p)
export_automation_event_list.restype = c_bool

set_automation_event_list = raylib_dll.SetAutomationEventList
set_automation_event_list.argtypes = (ctypes.POINTER(AutomationEventList),)
set_automation_event_list.restype = None

set_automation_event_base_frame = raylib_dll.SetAutomationEventBaseFrame
set_automation_event_base_frame.argtypes = (c_int,)
set_automation_event_base_frame.restype = None

start_automation_event_recording = raylib_dll.StartAutomationEventRecording
start_automation_event_recording.argtypes = None
start_automation_event_recording.restype = None

stop_automation_event_recording = raylib_dll.StopAutomationEventRecording
stop_automation_event_recording.argtypes = None
stop_automation_event_recording.restype = None

play_automation_event = raylib_dll.PlayAutomationEvent
play_automation_event.argtypes = (AutomationEvent,)
play_automation_event.restype = None

# Input-related functions: keyboard
is_key_pressed = raylib_dll.IsKeyPressed
is_key_pressed.argtypes = (c_int,)
is_key_pressed.restype = c_bool

is_key_pressed_repeat = raylib_dll.IsKeyPressedRepeat
is_key_pressed_repeat.argtypes = (c_int,)
is_key_pressed_repeat.restype = c_bool

is_key_down = raylib_dll.IsKeyDown
is_key_down.argtypes = (c_int,)
is_key_down.restype = c_bool

is_key_released = raylib_dll.IsKeyReleased
is_key_released.argtypes = (c_int,)
is_key_released.restype = c_bool

is_key_up = raylib_dll.IsKeyUp
is_key_up.argtypes = (c_int,)
is_key_up.restype = c_bool

get_key_pressed = raylib_dll.GetKeyPressed
get_key_pressed.argtypes = None
get_key_pressed.restype = c_int

get_char_pressed = raylib_dll.GetCharPressed
get_char_pressed.argtypes = None
get_char_pressed.restype = c_int

set_exit_key = raylib_dll.SetExitKey
set_exit_key.argtypes = (c_int,)
set_exit_key.restype = None

# Input-related functions: gamepads
is_gamepad_available = raylib_dll.IsGamepadAvailable
is_gamepad_available.argtypes = (c_int,)
is_gamepad_available.restype = c_bool

get_gamepad_name = raylib_dll.GetGamepadName
get_gamepad_name.argtypes = (c_int,)
get_gamepad_name.restype = c_char_p

is_gamepad_button_pressed = raylib_dll.IsGamepadButtonPressed
is_gamepad_button_pressed.argtypes = (c_int, c_int)
is_gamepad_button_pressed.restype = c_bool

is_gamepad_button_down = raylib_dll.IsGamepadButtonDown
is_gamepad_button_down.argtypes = (c_int, c_int)
is_gamepad_button_down.restype = c_bool

is_gamepad_button_released = raylib_dll.IsGamepadButtonReleased
is_gamepad_button_released.argtypes = (c_int, c_int)
is_gamepad_button_released.restype = c_bool

is_gamepad_button_up = raylib_dll.IsGamepadButtonUp
is_gamepad_button_up.argtypes = (c_int, c_int)
is_gamepad_button_up.restype = c_bool

get_gamepad_button = raylib_dll.GetGamepadButtonPressed
get_gamepad_button.argtypes = None
get_gamepad_button.restype = c_int

get_gamepad_axis_count = raylib_dll.GetGamepadAxisCount
get_gamepad_axis_count.argtypes = (c_int,)
get_gamepad_axis_count.restype = c_int

get_gamepad_axis_movement = raylib_dll.GetGamepadAxisMovement
get_gamepad_axis_movement.argtypes = (c_int, c_int)
get_gamepad_axis_movement.restype = c_float

set_gamepad_mappings = raylib_dll.SetGamepadMappings
set_gamepad_mappings.argtypes = (c_char_p,)
set_gamepad_mappings.restype = c_int

# Input-related functions: mouse
is_mouse_button_pressed = raylib_dll.IsMouseButtonPressed
is_mouse_button_pressed.argtypes = (c_int,)
is_mouse_button_pressed.restype = c_bool

is_mouse_button_down = raylib_dll.IsMouseButtonDown
is_mouse_button_down.argtypes = (c_int,)
is_mouse_button_down.restype = c_bool

is_mouse_button_released = raylib_dll.IsMouseButtonReleased
is_mouse_button_released.argtypes = (c_int,)
is_mouse_button_released.restype = c_bool

is_mouse_button_up = raylib_dll.IsMouseButtonUp
is_mouse_button_up.argtypes = (c_int,)
is_mouse_button_up.restype = c_bool

get_mouse_x = raylib_dll.GetMouseX
get_mouse_x.argtypes = None
get_mouse_x.restype = c_int

get_mouse_y = raylib_dll.GetMouseY
get_mouse_y.argtypes = None
get_mouse_y.restype = c_int

get_mouse_position = raylib_dll.GetMousePosition
get_mouse_position.argtypes = None
get_mouse_position.restype = Vector2

get_mouse_delta = raylib_dll.GetMouseDelta
get_mouse_delta.argtypes = None
get_mouse_delta.restype = Vector2

set_mouse_position = raylib_dll.SetMousePosition
set_mouse_position.argtypes = (c_int, c_int)
set_mouse_position.restype = None

set_mouse_offset = raylib_dll.SetMouseOffset
set_mouse_offset.argtypes = (c_int, c_int)
set_mouse_offset.restype = None

set_mouse_scale = raylib_dll.SetMouseScale
set_mouse_scale.argtypes = (c_float, c_float)
set_mouse_scale.restype = None

get_mouse_wheel_move = raylib_dll.GetMouseWheelMove
get_mouse_wheel_move.argtypes = None
get_mouse_wheel_move.restype = c_float

get_mouse_wheel_move_v = raylib_dll.GetMouseWheelMoveV
get_mouse_wheel_move_v.argtypes = None
get_mouse_wheel_move_v.restype = Vector2

set_mouse_cursor = raylib_dll.SetMouseCursor
set_mouse_cursor.argtypes = (c_int,)
set_mouse_cursor.restype = None

# Input-related functions: touch
get_touch_x = raylib_dll.GetTouchX
get_touch_x.argtypes = None
get_touch_x.restype = c_int

get_touch_y = raylib_dll.GetTouchY
get_touch_y.argtypes = None
get_touch_y.restype = c_int

get_touch_position = raylib_dll.GetTouchPosition
get_touch_position.argtypes = (c_int,)
get_touch_position.restype = Vector2

get_touch_point_id = raylib_dll.GetTouchPointId
get_touch_point_id.argtypes = (c_int,)
get_touch_point_id.restype = c_int

get_touch_point_count = raylib_dll.GetTouchPointCount
get_touch_point_count.argtypes = None
get_touch_point_count.restype = c_int

# Gestures and Touch Handling Functions (Module: rgestures)
set_gestures_enabled = raylib_dll.SetGesturesEnabled
set_gestures_enabled.argtypes = (c_uint,)
set_gestures_enabled.restype = None

is_gesture_detected = raylib_dll.IsGestureDetected
is_gesture_detected.argtypes = (c_uint,)
is_gesture_detected.restype = c_bool

get_gesture_detected = raylib_dll.GetGestureDetected
get_gesture_detected.argtypes = None
get_gesture_detected.restype = c_int

get_gesture_hold_duration = raylib_dll.GetGestureHoldDuration
get_gesture_hold_duration.argtypes = None
get_gesture_hold_duration.restype = c_float

get_gesture_drag_vector = raylib_dll.GetGestureDragVector
get_gesture_drag_vector.argtypes = None
get_gesture_drag_vector.restype = Vector2

get_gesture_drag_angle = raylib_dll.GetGestureDragAngle
get_gesture_drag_angle.argtypes = None
get_gesture_drag_angle.restype = c_float

get_gesture_pinch_vector = raylib_dll.GetGesturePinchVector
get_gesture_pinch_vector.argtypes = None
get_gesture_pinch_vector.restype = Vector2

get_gesture_pinch_angle = raylib_dll.GetGesturePinchAngle
get_gesture_pinch_angle.argtypes = None
get_gesture_pinch_angle.restype = c_float

# Camera System Functions (Module: rcamera)
update_camera = raylib_dll.UpdateCamera
update_camera.argtypes = (ctypes.POINTER(Camera), c_int)
update_camera.restype = None

update_camera_pro = raylib_dll.UpdateCameraPro
update_camera_pro.argtypes = (ctypes.POINTER(Camera), Vector3, Vector3, c_float)
update_camera_pro.restype = None

# Basic Shapes Drawing Functions (Module: shapes)
set_shapes_texture = raylib_dll.SetShapesTexture
set_shapes_texture.argtypes = (Texture2D, Rectangle)
set_shapes_texture.restype = None

# Basic shapes drawing functions
draw_pixel = raylib_dll.DrawPixel
draw_pixel.argtypes = (c_int, c_int, Color)
draw_pixel.restype = None

draw_pixel_v = raylib_dll.DrawPixelV
draw_pixel_v.argtypes = (Vector2, Color)
draw_pixel_v.restype = None

draw_line = raylib_dll.DrawLine
draw_line.argtypes = (c_int, c_int, c_int, c_int, Color)
draw_line.restype = None

draw_line_v = raylib_dll.DrawLineV
draw_line_v.argtypes = (Vector2, Vector2, Color)
draw_line_v.restype = None

draw_line_ex = raylib_dll.DrawLineEx
draw_line_ex.argtypes = (Vector2, Vector2, c_float, Color)
draw_line_ex.restype = None

draw_line_strip = raylib_dll.DrawLineStrip
draw_line_strip.argtypes = (Vector2, c_int, Color)
draw_line_strip.restype = None

draw_line_bezier = raylib_dll.DrawLineBezier
draw_line_bezier.argtypes = (Vector2, Vector2, c_float, Color)
draw_line_bezier.restype = None

draw_circle = raylib_dll.DrawCircle
draw_circle.argtypes = (c_int, c_int, c_float, Color)
draw_circle.restype = None

draw_circle_sector = raylib_dll.DrawCircleSector
draw_circle_sector.argtypes = (Vector2, c_float, c_float, c_float, c_int, Color)
draw_circle_sector.restype = None

draw_circle_sector_lines = raylib_dll.DrawCircleSectorLines
draw_circle_sector_lines.argtypes = (Vector2, c_float, c_float, c_float, c_int, Color)
draw_circle_sector_lines.restype = None

draw_circle_gradient = raylib_dll.DrawCircleGradient
draw_circle_gradient.argtypes = (c_int, c_int, c_float, Color, Color)
draw_circle_gradient.restype = None

draw_circle_v = raylib_dll.DrawCircleV
draw_circle_v.argtypes = (Vector2, c_float, Color)
draw_circle_v.restype = None

draw_circle_lines = raylib_dll.DrawCircleLines
draw_circle_lines.argtypes = (c_int, c_int, c_float, Color)
draw_circle_lines.restype = None

draw_circle_lines_v = raylib_dll.DrawCircleLinesV
draw_circle_lines_v.argtypes = (Vector2, c_float, Color)
draw_circle_lines_v.restype = None

draw_ellipse = raylib_dll.DrawEllipse
draw_ellipse.argtypes = (c_int, c_int, c_float, c_float, Color)
draw_ellipse.restype = None

draw_ellipse_lines = raylib_dll.DrawEllipseLines
draw_ellipse_lines.argtypes = (c_int, c_int, c_float, c_float, Color)
draw_ellipse_lines.restype = None

draw_ring = raylib_dll.DrawRing
draw_ring.argtypes = (Vector2, c_float, c_float, c_float, c_float, c_int, Color)
draw_ring.restype = None

draw_ring_lines = raylib_dll.DrawRingLines
draw_ring_lines.argtypes =(Vector2, c_float, c_float, c_float, c_float, c_int, Color)
draw_ring_lines.restype = None

draw_rectangle = raylib_dll.DrawRectangle
draw_rectangle.argtypes = (c_int, c_int, c_int, c_int, Color)
draw_rectangle.restype = None

draw_rectangle_v = raylib_dll.DrawRectangleV
draw_rectangle_v.argtypes = (Vector2, Vector2, Color)
draw_rectangle_v.restype = None

draw_rectangle_rec = raylib_dll.DrawRectangleRec
draw_rectangle_rec.argtypes = (Rectangle, Color)
draw_rectangle_rec.restype = None

draw_rectangle_pro = raylib_dll.DrawRectanglePro
draw_rectangle_pro.argtypes = (Rectangle, Vector2, c_float, Color)
draw_rectangle_pro.restype = None

draw_rectangle_gradient_v = raylib_dll.DrawRectangleGradientV
draw_rectangle_gradient_v.argtypes = (c_int, c_int, c_int, c_int, Color, Color)
draw_rectangle_gradient_v.restype = None

draw_rectangle_gradient_h = raylib_dll.DrawRectangleGradientH
draw_rectangle_gradient_h.argtypes = (c_int, c_int, c_int, c_int, Color, Color)
draw_rectangle_gradient_h.restype = None

draw_rectangle_gradient_ex = raylib_dll.DrawRectangleGradientEx
draw_rectangle_gradient_ex.argtypes = (Rectangle, Color, Color, Color, Color)
draw_rectangle_gradient_ex.restype = None

draw_rectangle_lines = raylib_dll.DrawRectangleLines
draw_rectangle_lines.argtypes = (c_int, c_int, c_int, c_int, Color)
draw_rectangle_lines.restype = None

draw_rectangle_lines_ex = raylib_dll.DrawRectangleLinesEx
draw_rectangle_lines_ex.argtypes = (Rectangle, c_float, Color)
draw_rectangle_lines_ex.restype = None

draw_rectangle_rounded = raylib_dll.DrawRectangleRounded
draw_rectangle_rounded.argtypes = (Rectangle, c_float, c_int, Color)
draw_rectangle_rounded.restype = None

draw_rectangle_rounded_lines = raylib_dll.DrawRectangleRoundedLines
draw_rectangle_rounded_lines.argtypes = (Rectangle, c_float, c_int, c_float, Color)
draw_rectangle_rounded_lines.restype = None

draw_triangle = raylib_dll.DrawTriangle
draw_triangle.argtypes = (Vector2, Vector2, Vector2, Color)
draw_triangle.restype = None

draw_triangle_lines = raylib_dll.DrawTriangleLines
draw_triangle_lines.argtypes = (Vector2, Vector2, Vector2, Color)
draw_triangle_lines.restype = None

draw_triangle_fan = raylib_dll.DrawTriangleFan
draw_triangle_fan.argtypes =(Vector2, c_int, Color)
draw_triangle_fan.restype = None

draw_triangle_strip = raylib_dll.DrawTriangleStrip
draw_triangle_strip.argtypes = (Vector2, c_int, Color)
draw_triangle_strip.restype = None

draw_poly = raylib_dll.DrawPoly
draw_poly.argtypes = (Vector2, c_int, c_float, c_float, Color)
draw_poly.restype = None

draw_poly_lines = raylib_dll.DrawPolyLines
draw_poly_lines.argtypes = (Vector2, c_int, c_float, c_float, Color)
draw_poly_lines.restype = None

draw_poly_lines_ex = raylib_dll.DrawPolyLinesEx
draw_poly_lines_ex.argtypes = (Vector2, c_int, c_float, c_float, c_float, Color)
draw_poly_lines_ex.restype = None

# Splines drawing functions
draw_spline_linear = raylib_dll.DrawSplineLinear
draw_spline_linear.argtypes = (ctypes.POINTER(Vector2), c_int, c_float, Color)
draw_spline_linear.restype = None

draw_spline_basis = raylib_dll.DrawSplineBasis
draw_spline_basis.argtypes = (ctypes.POINTER(Vector2), c_int, c_float, Color)
draw_spline_basis.restype = None

draw_spline_catmull_rom = raylib_dll.DrawSplineCatmullRom
draw_spline_catmull_rom.argtypes = (ctypes.POINTER(Vector2), c_int, c_float, Color)
draw_spline_catmull_rom.restype = None

draw_spline_bezier_quadratic = raylib_dll.DrawSplineBezierQuadratic
draw_spline_bezier_quadratic.argtypes = (ctypes.POINTER(Vector2), c_int, c_float, Color)
draw_spline_bezier_quadratic.restype = None

draw_spline_bezier_cubic = raylib_dll.DrawSplineBezierCubic
draw_spline_bezier_cubic.argtypes = (ctypes.POINTER(Vector2), c_int, c_float, Color)
draw_spline_bezier_cubic.restype = None

draw_spline_segment_linear = raylib_dll.DrawSplineSegmentLinear
draw_spline_segment_linear.argtypes = (Vector2, Vector2, c_float, Color)
draw_spline_segment_linear.restype = None

draw_spline_segment_basis = raylib_dll.DrawSplineSegmentBasis
draw_spline_segment_basis.argtypes = (Vector2, Vector2, Vector2, Vector2, c_float, Color)
draw_spline_segment_basis.restype = None

draw_spline_segment_catmull_rom = raylib_dll.DrawSplineSegmentCatmullRom
draw_spline_segment_catmull_rom.argtypes = (Vector2, Vector2, Vector2, Vector2, c_float, Color)
draw_spline_segment_catmull_rom.restype = None

draw_spline_segment_bezier_quadratic = raylib_dll.DrawSplineSegmentBezierQuadratic
draw_spline_segment_bezier_quadratic.argtypes = (Vector2, Vector2, Vector2, c_float, Color)
draw_spline_segment_bezier_quadratic.restype = None

draw_spline_segment_bezier_cubic = raylib_dll.DrawSplineSegmentBezierCubic
draw_spline_segment_bezier_cubic.argtypes = (Vector2, Vector2, Vector2, Vector2, c_float, Color)
draw_spline_segment_bezier_cubic.restype = None

# Spline segment point evaluation functions, for a given t [0.0f .. 1.0f]
get_spline_point_linear = raylib_dll.GetSplinePointLinear
get_spline_point_linear.argtypes = (Vector2, Vector2, c_float)
get_spline_point_linear.restype = Vector2

get_spline_point_basis = raylib_dll.GetSplinePointBasis
get_spline_point_basis.argtypes = (Vector2, Vector2, Vector2, Vector2, c_float)
get_spline_point_basis.restype = Vector2

get_spline_point_catmull_rom = raylib_dll.GetSplinePointCatmullRom
get_spline_point_catmull_rom.argtypes = (Vector2, Vector2, Vector2, Vector2, c_float)
get_spline_point_catmull_rom.restype = Vector2

get_spline_point_bezier_quad = raylib_dll.GetSplinePointBezierQuad
get_spline_point_bezier_quad.argtypes = (Vector2, Vector2, Vector2, c_float)
get_spline_point_bezier_quad.restype = Vector2

get_spline_point_bezier_cubic = raylib_dll.GetSplinePointBezierCubic
get_spline_point_bezier_cubic.argtypes = (Vector2, Vector2, Vector2, Vector2, c_float)
get_spline_point_bezier_cubic.restype = Vector2

# Basic shapes collision detection functions
check_collision_recs = raylib_dll.CheckCollisionRecs
check_collision_recs.argtypes = (Rectangle, Rectangle)
check_collision_recs.restype = c_bool

check_collision_circles = raylib_dll.CheckCollisionCircles
check_collision_circles.argtypes = (Vector2, c_float, Vector2, c_float)
check_collision_circles.restype = c_bool

check_collision_circle_rec = raylib_dll.CheckCollisionCircleRec
check_collision_circle_rec.argtypes = (Vector2, c_float, Rectangle)
check_collision_circle_rec.restype = c_bool

check_collision_point_rec = raylib_dll.CheckCollisionPointRec
check_collision_point_rec.argtypes = (Vector2, Rectangle)
check_collision_point_rec.restype = c_bool

check_collision_point_circle = raylib_dll.CheckCollisionPointCircle
check_collision_point_circle.argtypes = (Vector2, Vector2, c_float)
check_collision_point_circle.restype = c_bool

check_collision_point_triangle = raylib_dll.CheckCollisionPointTriangle
check_collision_point_triangle.argtypes = (Vector2, Vector2, Vector2, Vector2)
check_collision_point_triangle.restype = c_bool

check_collision_point_poly = raylib_dll.CheckCollisionPointPoly
check_collision_point_poly.argtypes = (Vector2, ctypes.POINTER(Vector2), c_int)
check_collision_point_poly.restype = c_bool

check_collision_lines = raylib_dll.CheckCollisionLines
check_collision_lines.argtypes = (Vector2, Vector2, Vector2, Vector2, ctypes.POINTER(Vector2))
check_collision_lines.restype = c_bool

check_collision_point_line = raylib_dll.CheckCollisionPointLine
check_collision_point_line.argtypes = (Vector2, Vector2, Vector2, c_int)
check_collision_point_line.restype = c_bool

get_collision_rec = raylib_dll.GetCollisionRec
get_collision_rec.argtypes = (Rectangle, Rectangle)
get_collision_rec.restype = Rectangle

# Texture Loading and Drawing Functions (Module: textures)

# Image loading functions
# NOTE: These functions do not require GPU access
load_image = raylib_dll.LoadImage
load_image.argtypes = (c_char_p,)
load_image.restype = Image

load_image_raw = raylib_dll.LoadImageRaw
load_image_raw.argtypes = (c_char_p, c_int, c_int, c_int, c_int)
load_image_raw.restype = Image

load_image_svg = raylib_dll.LoadImageSvg
load_image_svg.argtypes = (c_char_p, c_int, c_int)
load_image_svg.restype = Image

load_image_anim = raylib_dll.LoadImageAnim
load_image_anim.argtypes = (c_char_p, ctypes.POINTER(c_int))
load_image_anim.restype = Image

load_image_from_memory = raylib_dll.LoadImageFromMemory
load_image_from_memory.argtypes = (c_char_p, ctypes.POINTER(c_ubyte), c_int)
load_image_from_memory.restype = Image

load_image_from_texture = raylib_dll.LoadImageFromTexture
load_image_from_texture.argtypes = (Texture2D,)
load_image_from_texture.restype = Image

load_image_from_screen = raylib_dll.LoadImageFromScreen
load_image_from_screen.argtypes = None
load_image_from_screen.restype = Image

is_image_ready = raylib_dll.IsImageReady
is_image_ready.argtypes = (Image,)
is_image_ready.restype = c_bool

unload_image = raylib_dll.UnloadImage
unload_image.argtypes = (Image,)
unload_image.restype = None

export_image = raylib_dll.ExportImage
export_image.argtypes = (Image, c_char_p)
export_image.restype = c_bool

export_image_to_memory = raylib_dll.ExportImageToMemory
export_image_to_memory.argtypes = (Image, c_char_p, ctypes.POINTER(c_int))
export_image_to_memory.restype = ctypes.POINTER(c_ubyte)

export_image_as_code = raylib_dll.ExportImageAsCode
export_image_as_code.argtypes = (Image, c_char_p)
export_image_as_code.restype = c_bool

# Image generation functions
gen_image_color = raylib_dll.GenImageColor
gen_image_color.argtypes = (c_int, c_int, Color)
gen_image_color.restype = Image

gen_image_gradient_linear = raylib_dll.GenImageGradientLinear
gen_image_gradient_linear.argtypes = (c_int, c_int, c_int, Color, Color)
gen_image_gradient_linear.restype = Image

gen_image_gradient_radial = raylib_dll.GenImageGradientRadial
gen_image_gradient_radial.argtypes = (c_int, c_int, c_float, Color, Color)
gen_image_gradient_radial.restype = Image

gen_image_gradient_square = raylib_dll.GenImageGradientSquare
gen_image_gradient_square.argtypes = (c_int, c_int, c_float, Color, Color)
gen_image_gradient_square.restype = Image

gen_image_checked = raylib_dll.GenImageChecked
gen_image_checked.argtypes = (c_int, c_int, c_int, c_int, Color, Color)
gen_image_checked.restype = Image

gen_image_white_noise = raylib_dll.GenImageWhiteNoise
gen_image_white_noise.argtypes = (c_int, c_int, c_float)
gen_image_white_noise.restype = Image

gen_image_perlin_noise = raylib_dll.GenImagePerlinNoise
gen_image_perlin_noise.argtypes = (c_int, c_int, c_int, c_int, c_float)
gen_image_perlin_noise.restype = Image

gen_image_cellular = raylib_dll.GenImageCellular
gen_image_cellular.argtypes = (c_int, c_int, c_int)
gen_image_cellular.restype = Image

gen_image_text = raylib_dll.GenImageText
gen_image_text.argtypes = (c_int, c_int, c_char_p)
gen_image_text.restype = Image

# Image manipulation functions
image_copy = raylib_dll.ImageCopy
image_copy.argtypes = (Image,)
image_copy.restype = Image

image_from_image = raylib_dll.ImageFromImage
image_from_image.argtypes = (Image, Rectangle)
image_from_image.restype = Image

image_text = raylib_dll.ImageText
image_text.argtypes = (c_char_p, c_int, Color)
image_text.restype = Image

image_text_ex = raylib_dll.ImageTextEx
image_text_ex.argtypes = (Font, c_char_p, c_float, c_float, Color)
image_text_ex.restype = Image

image_format = raylib_dll.ImageFormat
image_format.argtypes = (ctypes.POINTER(Image), c_int)
image_format.restype = None

image_to_pot = raylib_dll.ImageToPOT
image_to_pot.argtypes = (ctypes.POINTER(Image), Color)
image_to_pot.restype = None

image_crop = raylib_dll.ImageCrop
image_crop.argtypes = (ctypes.POINTER(Image), Rectangle)
image_crop.restype = None

image_alpha_crop = raylib_dll.ImageAlphaCrop
image_alpha_crop.argtypes = (ctypes.POINTER(Image), c_float)
image_alpha_crop.restype = None

image_alpha_clear = raylib_dll.ImageAlphaClear
image_alpha_clear.argtypes = (ctypes.POINTER(Image), Color, c_float)
image_alpha_clear.restype = None

image_alpha_mask = raylib_dll.ImageAlphaMask
image_alpha_mask.argtypes = (ctypes.POINTER(Image), Image)
image_alpha_mask.restype = None

image_alpha_premultiply = raylib_dll.ImageAlphaPremultiply
image_alpha_premultiply.argtypes = (ctypes.POINTER(Image),)
image_alpha_premultiply.restype = None

image_blur_gaussian = raylib_dll.ImageBlurGaussian
image_blur_gaussian.argtypes = (ctypes.POINTER(Image), c_int)
image_blur_gaussian.restype = None

image_resize = raylib_dll.ImageResize
image_resize.argtypes = (ctypes.POINTER(Image), c_int, c_int)
image_resize.restype = None

image_resize_nn = raylib_dll.ImageResizeNN
image_resize_nn.argtypes = (ctypes.POINTER(Image), c_int, c_int)
image_resize_nn.restype = None

image_resize_canvas = raylib_dll.ImageResizeCanvas
image_resize_canvas.argtypes = (ctypes.POINTER(Image), c_int, c_int, c_int, c_int, Color)
image_resize_canvas.restype = None

image_mipmaps = raylib_dll.ImageMipmaps
image_mipmaps.argtypes = (ctypes.POINTER(Image),)
image_mipmaps.restype = None

image_dither = raylib_dll.ImageDither
image_dither.argtypes = (ctypes.POINTER(Image), c_int, c_int, c_int, c_int)
image_dither.restype = None

image_flip_vertical = raylib_dll.ImageFlipVertical
image_flip_vertical.argtypes = (ctypes.POINTER(Image),)
image_flip_vertical.restype = None

image_flip_horizontal = raylib_dll.ImageFlipHorizontal
image_flip_horizontal.argtypes = (ctypes.POINTER(Image),)
image_flip_horizontal.restype = None

image_rotate = raylib_dll.ImageRotate
image_rotate.argtypes = (ctypes.POINTER(Image), c_int)
image_rotate.restype = None

image_rotate_cw = raylib_dll.ImageRotateCW
image_rotate_cw.argtypes = (ctypes.POINTER(Image),)
image_rotate_cw.restype = None

image_rotate_ccw = raylib_dll.ImageRotateCCW
image_rotate_ccw.argtypes = (ctypes.POINTER(Image),)
image_rotate_ccw.restype = None

image_color_tint = raylib_dll.ImageColorTint
image_color_tint.argtypes = (ctypes.POINTER(Image), Color)
image_color_tint.restype = None

image_color_invert = raylib_dll.ImageColorInvert
image_color_invert.argtypes = (ctypes.POINTER(Image),)
image_color_invert.restype = None

image_color_grayscale = raylib_dll.ImageColorGrayscale
image_color_grayscale.argtypes = (ctypes.POINTER(Image),)
image_color_grayscale.restype = None

image_color_contrast = raylib_dll.ImageColorContrast
image_color_contrast.argtypes = (ctypes.POINTER(Image), c_float)
image_color_contrast.restype = None

image_color_brightness = raylib_dll.ImageColorBrightness
image_color_brightness.argtypes = (ctypes.POINTER(Image), c_int)
image_color_brightness.restype = None

image_color_replace = raylib_dll.ImageColorReplace
image_color_replace.argtypes = (ctypes.POINTER(Image), Color, Color)
image_color_replace.restype = None

load_image_colors = raylib_dll.LoadImageColors
load_image_colors.argtypes = (Image,)
load_image_colors.restype = ctypes.POINTER(Color)

load_image_palette = raylib_dll.LoadImagePalette
load_image_palette.argtypes = (Image, c_int, ctypes.POINTER(c_int))
load_image_palette.restype = ctypes.POINTER(Color)

unload_image_colors = raylib_dll.UnloadImageColors
unload_image_colors.argtypes = (ctypes.POINTER(Color),)
unload_image_colors.restype = None

unload_image_palette = raylib_dll.UnloadImagePalette
unload_image_palette.argtypes = (ctypes.POINTER(Color),)
unload_image_palette.restype = None

get_image_alpha_border = raylib_dll.GetImageAlphaBorder
get_image_alpha_border.argtypes = (Image, c_float)
get_image_alpha_border.restype = Rectangle

get_image_color = raylib_dll.GetImageColor
get_image_color.argtypes = (Image, c_int, c_int)
get_image_color.restype = Color

# Image drawing functions
# NOTE: Image software-rendering functions (CPU)
image_clear_background = raylib_dll.ImageClearBackground
image_clear_background.argtypes = (ctypes.POINTER(Image), Color)
image_clear_background.restype = None

image_draw_pixel = raylib_dll.ImageDrawPixel
image_draw_pixel.argtypes = (ctypes.POINTER(Image), c_int, c_int, Color)
image_draw_pixel.restype = None

image_draw_pixel_v = raylib_dll.ImageDrawPixelV
image_draw_pixel_v.argtypes = (ctypes.POINTER(Image), Vector2, Color)
image_draw_pixel_v.restype = None

image_draw_line = raylib_dll.ImageDrawLine
image_draw_line.argtypes = (ctypes.POINTER(Image), c_int, c_int, c_int, c_int, Color)
image_draw_line.restype = None

image_draw_line_v = raylib_dll.ImageDrawLineV
image_draw_line_v.argtypes = (ctypes.POINTER(Image), Vector2, Vector2, Color)
image_draw_line_v.restype = None

image_draw_circle = raylib_dll.ImageDrawCircle
image_draw_circle.argtypes = (ctypes.POINTER(Image), c_int, c_int, c_int, Color)
image_draw_circle.restype = None

image_draw_circle_v = raylib_dll.ImageDrawCircleV
image_draw_circle_v.argtypes = (ctypes.POINTER(Image), Vector2, c_int, Color)
image_draw_circle_v.restype = None

image_draw_circle_lines = raylib_dll.ImageDrawCircleLines
image_draw_circle_lines.argtypes = (ctypes.POINTER(Image), c_int, c_int, c_int, Color)
image_draw_circle_lines.restype = None

image_draw_circle_lines_v = raylib_dll.ImageDrawCircleLinesV
image_draw_circle_lines_v.argtypes = (ctypes.POINTER(Image), Vector2, c_int, Color)
image_draw_circle_lines_v.restype = None

image_draw_rectangle = raylib_dll.ImageDrawRectangle
image_draw_rectangle.argtypes = (ctypes.POINTER(Image), c_int, c_int, c_int, c_int, Color)
image_draw_rectangle.restype = None

image_draw_rectangle_v = raylib_dll.ImageDrawRectangleV
image_draw_rectangle_v.argtypes = (ctypes.POINTER(Image), Vector2, Vector2, Color)
image_draw_rectangle_v.restype = None

image_draw_rectangle_rec = raylib_dll.ImageDrawRectangleRec
image_draw_rectangle_rec.argtypes = (ctypes.POINTER(Image), Rectangle, Color)
image_draw_rectangle_rec.restype = None

image_draw_rectangle_lines = raylib_dll.ImageDrawRectangleLines
image_draw_rectangle_lines.argtypes = (ctypes.POINTER(Image), Rectangle, c_int, Color)
image_draw_rectangle_lines.restype = None

image_draw = raylib_dll.ImageDraw
image_draw.argtypes = (ctypes.POINTER(Image), Image, Rectangle, Rectangle, Color)
image_draw.restype = None

image_draw_text = raylib_dll.ImageDrawText
image_draw_text.argtypes = (ctypes.POINTER(Image), c_char_p, c_int, c_int, c_int, Color)
image_draw_text.restype = None

image_draw_text_ex = raylib_dll.ImageDrawTextEx
image_draw_text_ex.argtypes = (ctypes.POINTER(Image), Font, c_char_p, Vector2, c_float, c_float, Color)
image_draw_text_ex.restype = None

# Texture loading functions
# NOTE: These functions require GPU access
load_texture = raylib_dll.LoadTexture
load_texture.argtypes = (c_char_p,)
load_texture.restype = Texture2D

load_texture_from_image = raylib_dll.LoadTextureFromImage
load_texture_from_image.argtypes = (Image,)
load_texture_from_image.restype = Texture2D

load_texture_cubemap = raylib_dll.LoadTextureCubemap
load_texture_cubemap.argtypes = (Image, c_int)
load_texture_cubemap.restype = TextureCubemap

load_render_texture = raylib_dll.LoadRenderTexture
load_render_texture.argtypes = (c_int, c_int)
load_render_texture.restype = RenderTexture2D

is_texture_ready = raylib_dll.IsTextureReady
is_texture_ready.argtypes = (Texture2D,)
is_texture_ready.restype = c_bool

unload_texture = raylib_dll.UnloadTexture
unload_texture.argtypes = (Texture2D,)
unload_texture.restype = None

is_render_texture_ready = raylib_dll.IsRenderTextureReady
is_render_texture_ready.argtypes = (RenderTexture2D,)
is_render_texture_ready.restype = c_bool

unload_render_texture = raylib_dll.UnloadRenderTexture
unload_render_texture.argtypes = (RenderTexture2D,)
unload_render_texture.restype = None

update_texture = raylib_dll.UpdateTexture
update_texture.argtypes = (Texture2D, c_void_p)
update_texture.restype = None

update_texture_rec = raylib_dll.UpdateTextureRec
update_texture_rec.argtypes = (Texture2D, Rectangle, c_void_p)
update_texture_rec.restype = None

# Texture configuration functions
gen_texture_mipmaps = raylib_dll.GenTextureMipmaps
gen_texture_mipmaps.argtypes = (ctypes.POINTER(Texture2D),)
gen_texture_mipmaps.restype = None

set_texture_filter = raylib_dll.SetTextureFilter
set_texture_filter.argtypes = (Texture2D, c_int)
set_texture_filter.restype = None

set_texture_wrap = raylib_dll.SetTextureWrap
set_texture_wrap.argtypes = (Texture2D, c_int)
set_texture_wrap.restype = None

# Texture drawing functions
draw_texture = raylib_dll.DrawTexture
draw_texture.argtypes = (Texture2D, c_int, c_int, Color)
draw_texture.restype = None

draw_texture_v = raylib_dll.DrawTextureV
draw_texture_v.argtypes = (Texture2D, Vector2, Color)
draw_texture_v.restype = None

draw_texture_ex = raylib_dll.DrawTextureEx
draw_texture_ex.argtypes = (Texture2D, Vector2, c_float, c_float, Color)
draw_texture_ex.restype = None

draw_texture_rec = raylib_dll.DrawTextureRec
draw_texture_rec.argtypes = (Texture2D, Rectangle, Vector2, Color)
draw_texture_rec.restype = None

draw_texture_pro = raylib_dll.DrawTexturePro
draw_texture_pro.argtypes = (Texture2D, Rectangle, Rectangle, Vector2, c_float, Color)
draw_texture_pro.restype = None

draw_texture_n_patch = raylib_dll.DrawTextureNPatch
draw_texture_n_patch.argtypes = (Texture2D, NPatchInfo, Rectangle, Vector2, c_float, Color)
draw_texture_n_patch.restype = None

# Color/pixel related functions
fade = raylib_dll.Fade
fade.argtypes = (Color, c_float)
fade.restype = Color

color_to_int = raylib_dll.ColorToInt
color_to_int.argtypes = (Color,)
color_to_int.restype = c_int

color_normalize = raylib_dll.ColorNormalize
color_normalize.argtypes = (Color,)
color_normalize.restype = Vector4

color_from_normalized = raylib_dll.ColorFromNormalized
color_from_normalized.argtypes = (Vector4,)
color_from_normalized.restype = Color

color_to_hsv = raylib_dll.ColorToHSV
color_to_hsv.argtypes = (Color,)
color_to_hsv.restype = Vector3

color_from_hsv = raylib_dll.ColorFromHSV
color_from_hsv.argtypes = (c_float, c_float, c_float)
color_from_hsv.restype = Color

color_tint = raylib_dll.ColorTint
color_tint.argtypes = (Color, Color)
color_tint.restype = Color

color_brightness = raylib_dll.ColorBrightness
color_brightness.argtypes = (Color, c_float)
color_brightness.restype = Color

color_contrast = raylib_dll.ColorContrast
color_contrast.argtypes = (Color, c_float)
color_contrast.restype = Color

color_alpha = raylib_dll.ColorAlpha
color_alpha.argtypes = (Color, c_float)
color_alpha.restype = Color

color_alpha_blend = raylib_dll.ColorAlphaBlend
color_alpha_blend.argtypes = (Color, Color, Color)
color_alpha_blend.restype = Color

get_color = raylib_dll.GetColor
get_color.argtypes = (c_uint,)
get_color.restype = Color

get_pixel_color = raylib_dll.GetPixelColor
get_pixel_color.argtypes = (c_void_p, c_int)
get_pixel_color.restype = Color

set_pixel_color = raylib_dll.SetPixelColor
set_pixel_color.argtypes = (c_void_p, Color, c_int)
set_pixel_color.restype = None

get_pixel_data_size = raylib_dll.GetPixelDataSize
get_pixel_data_size.argtypes = (c_int, c_int, c_int)
get_pixel_data_size.restype = c_int

# Font Loading and Text Drawing Functions (Module: text)

# Font loading/unloading functions
get_font_default = raylib_dll.GetFontDefault
get_font_default.argtypes = None
get_font_default.restype = Font

load_font = raylib_dll.LoadFont
load_font.argtypes = (c_char_p,)
load_font.restype = Font

load_font_ex = raylib_dll.LoadFontEx
load_font_ex.argtypes = (c_char_p, c_int, ctypes.POINTER(c_int), c_int)
load_font_ex.restype = Font

load_font_from_image = raylib_dll.LoadFontFromImage
load_font_from_image.argtypes = (Image, Color, c_int)
load_font_from_image.restype = Font

load_font_from_memory = raylib_dll.LoadFontFromMemory
load_font_from_memory.argtypes = (c_char_p, ctypes.POINTER(c_ubyte), c_int, c_int, ctypes.POINTER(c_int), c_int)
load_font_from_memory.restype = Font

is_font_ready = raylib_dll.IsFontReady
is_font_ready.argtypes = (Font,)
is_font_ready.restype = c_bool

load_font_data = raylib_dll.LoadFontData
load_font_data.argtypes = (ctypes.POINTER(c_ubyte), c_int, c_int, ctypes.POINTER(c_int), c_int, c_int)
load_font_data.restype = ctypes.POINTER(GlyphInfo)

gen_image_font_atlas = raylib_dll.GenImageFontAtlas
gen_image_font_atlas.argtypes = (ctypes.POINTER(GlyphInfo), ctypes.POINTER(Rectangle), c_int, c_int, c_int, c_int)
gen_image_font_atlas.restype = Image

unload_font_data = raylib_dll.UnloadFontData
unload_font_data.argtypes = (ctypes.POINTER(GlyphInfo), c_int)
unload_font_data.restype = None

unload_font = raylib_dll.UnloadFont
unload_font.argtypes = (Font,)
unload_font.restype = None

export_font_as_code = raylib_dll.ExportFontAsCode
export_font_as_code.argtypes = (Font, c_char_p)
export_font_as_code.restype = c_bool

# Text drawing functions
draw_fps = raylib_dll.DrawFPS
draw_fps.argtypes = (c_int, c_int)
draw_fps.restype = None

draw_text = raylib_dll.DrawText
draw_text.argtypes = (c_char_p, c_int, c_int, c_int, Color)
draw_text.restype = None

draw_text_ex = raylib_dll.DrawTextEx
draw_text_ex.argtypes = (Font, c_char_p, Vector2, c_float, c_float, Color)
draw_text_ex.restype = None

draw_text_pro = raylib_dll.DrawTextPro
draw_text_pro.argtypes = (Font, c_char_p, Vector2, Vector2, c_float, c_float, c_float, Color)
draw_text_pro.restype = None

draw_text_codepoint = raylib_dll.DrawTextCodepoint
draw_text_codepoint.argtypes = (Font, c_int, Vector2, c_float, Color)
draw_text_codepoint.restype = None

draw_text_codepoints = raylib_dll.DrawTextCodepoints
draw_text_codepoints.argtypes = (Font, ctypes.POINTER(c_int), c_int, Vector2, c_float, c_float, Color)
draw_text_codepoints.restype = None

# Text font info functions
set_text_line_spacing = raylib_dll.SetTextLineSpacing
set_text_line_spacing.argtypes = (c_int,)
set_text_line_spacing.restype = None

measure_text = raylib_dll.MeasureText
measure_text.argtypes = (c_char_p, c_int)
measure_text.restype = c_int

measure_text_ex = raylib_dll.MeasureTextEx
measure_text_ex.argtypes = (Font, c_char_p, c_float, c_float)
measure_text_ex.restype = Vector2

get_glyph_index = raylib_dll.GetGlyphIndex
get_glyph_index.argtypes = (Font, c_int)
get_glyph_index.restype = c_int

get_glyph_info = raylib_dll.GetGlyphInfo
get_glyph_info.argtypes = (Font, c_int)
get_glyph_info.restype = GlyphInfo

get_glyph_atlas_rec = raylib_dll.GetGlyphAtlasRec
get_glyph_atlas_rec.argtypes = (Font, c_int)
get_glyph_atlas_rec.restype = Rectangle

# Text codepoints management functions (unicode characters)
load_utf8 = raylib_dll.LoadUTF8
load_utf8.argtypes = (ctypes.POINTER(c_int), c_int)
load_utf8.restype = c_char_p

unload_utf8 = raylib_dll.UnloadUTF8
unload_utf8.argtypes = (c_char_p,)
unload_utf8.restype = None

load_codepoints = raylib_dll.LoadCodepoints
load_codepoints.argtypes = (c_char_p, ctypes.POINTER(c_int))
load_codepoints.restype = ctypes.POINTER(c_int)

unload_codepoints = raylib_dll.UnloadCodepoints
unload_codepoints.argtypes = (ctypes.POINTER(c_int),)
unload_codepoints.restype = None

get_codepoint_count = raylib_dll.GetCodepointCount
get_codepoint_count.argtypes = (c_char_p,)
get_codepoint_count.restype = c_int

get_codepoint = raylib_dll.GetCodepoint
get_codepoint.argtypes = (c_char_p, ctypes.POINTER(c_int))
get_codepoint.restype = c_int

get_codepoint_next = raylib_dll.GetCodepointNext
get_codepoint_next.argtypes = (c_char_p, ctypes.POINTER(c_int))
get_codepoint_next.restype = c_int

get_codepoint_previous = raylib_dll.GetCodepointPrevious
get_codepoint_previous.argtypes = (c_char_p, ctypes.POINTER(c_int))
get_codepoint_previous.restype = c_int

codepoint_to_utf8 = raylib_dll.CodepointToUTF8
codepoint_to_utf8.argtypes = (c_int, ctypes.POINTER(c_int))
codepoint_to_utf8.restype = c_char_p

# Text strings management functions (no UTF-8 strings, only byte chars)
# NOTE: Some strings allocate memory internally for returned strings, just be careful!
text_copy = raylib_dll.TextCopy
text_copy.argtypes = (c_char_p, c_char_p)
text_copy.restype = c_int

text_is_equal = raylib_dll.TextIsEqual
text_is_equal.argtypes = (c_char_p, c_char_p)
text_is_equal.restype = c_bool

text_length = raylib_dll.TextLength
text_length.argtypes = (c_char_p,)
text_length.restype = c_uint

text_format = raylib_dll.TextFormat
text_format.argtypes = (c_char_p,)
text_format.restype = c_char_p

text_subtext = raylib_dll.TextSubtext
text_subtext.argtypes = (c_char_p, c_int, c_int)
text_subtext.restype = c_char_p

text_replace = raylib_dll.TextReplace
text_replace.argtypes = (c_char_p, c_char_p, c_char_p)
text_replace.restype = c_char_p

text_insert = raylib_dll.TextInsert
text_insert.argtypes = (c_char_p, c_char_p, c_int)
text_insert.restype = c_char_p

text_join = raylib_dll.TextJoin
text_join.argtypes = (c_char_p, c_int, c_char_p)
text_join.restype = c_char_p

text_split = raylib_dll.TextSplit
text_split.argtypes = (c_char_p, c_byte, ctypes.POINTER(c_int))
text_split.restype = ctypes.POINTER(ctypes.POINTER(c_byte))

text_append = raylib_dll.TextAppend
text_append.argtypes = (c_char_p, c_char_p, ctypes.POINTER(c_int))
text_append.restype = None

text_find_index = raylib_dll.TextFindIndex
text_find_index.argtypes = (c_char_p, c_char_p)
text_find_index.restype = c_int

text_to_upper = raylib_dll.TextToUpper
text_to_upper.argtypes = (c_char_p,)
text_to_upper.restype = c_char_p

text_to_lower = raylib_dll.TextToLower
text_to_lower.argtypes = (c_char_p,)
text_to_lower.restype = c_char_p

text_to_pascal = raylib_dll.TextToPascal
text_to_pascal.argtypes = (c_char_p,)
text_to_pascal.restype = c_char_p

text_to_integer = raylib_dll.TextToInteger
text_to_integer.argtypes = (c_char_p,)
text_to_integer.restype = c_int

# Basic 3d Shapes Drawing Functions (Module: models)

# Basic geometric 3D shapes drawing functions
draw_line_3d = raylib_dll.DrawLine3D
draw_line_3d.argtypes = (Vector3, Vector3, Color)
draw_line_3d.restype = None

draw_point_3d = raylib_dll.DrawPoint3D
draw_point_3d.argtypes = (Vector3, Color)
draw_point_3d.restype = None

draw_circle_3d = raylib_dll.DrawCircle3D
draw_circle_3d.argtypes = (Vector3, c_float, Vector3, c_float, Color)
draw_circle_3d.restype = None

draw_triangle_3d = raylib_dll.DrawTriangle3D
draw_triangle_3d.argtypes = (Vector3, Vector3, Vector3, Color)
draw_triangle_3d.restype = None

draw_triangle_strip_3d = raylib_dll.DrawTriangleStrip3D
draw_triangle_strip_3d.argtypes = (ctypes.POINTER(Vector3), c_int, Color)
draw_triangle_strip_3d.restype = None

draw_cube = raylib_dll.DrawCube
draw_cube.argtypes = (Vector3, c_float, c_float, c_float, Color)
draw_cube.restype = None

draw_cube_v = raylib_dll.DrawCubeV
draw_cube_v.argtypes = (Vector3, Vector3, Color)
draw_cube_v.restype = None

draw_cube_wires = raylib_dll.DrawCubeWires
draw_cube_wires.argtypes = (Vector3, c_float, c_float, c_float, Color)
draw_cube_wires.restype = None

draw_cube_wires_v = raylib_dll.DrawCubeWiresV
draw_cube_wires_v.argtypes = (Vector3, Vector3, Color)
draw_cube_wires_v.restype = None

draw_sphere = raylib_dll.DrawSphere
draw_sphere.argtypes = (Vector3, c_float, Color)
draw_sphere.restype = None

draw_sphere_ex = raylib_dll.DrawSphereEx
draw_sphere_ex.argtypes = (Vector3, c_float, c_int, c_int, Color)
draw_sphere_ex.restype = None

draw_sphere_wires = raylib_dll.DrawSphereWires
draw_sphere_wires.argtypes = (Vector3, c_float, c_int, c_int, Color)
draw_sphere_wires.restype = None

draw_cylinder = raylib_dll.DrawCylinder
draw_cylinder.argtypes = (Vector3, c_float, c_float, c_float, c_int, Color)
draw_cylinder.restype = None

draw_cylinder_ex = raylib_dll.DrawCylinderEx
draw_cylinder_ex.argtypes = (Vector3, Vector3, c_float, c_float, c_int, Color)
draw_cylinder_ex.restype = None

draw_cylinder_wires = raylib_dll.DrawCylinderWires
draw_cylinder_wires.argtypes = (Vector3, c_float, c_float, c_float, c_int, Color)
draw_cylinder_wires.restype = None

draw_cylinder_wires_ex = raylib_dll.DrawCylinderWiresEx
draw_cylinder_wires_ex.argtypes = (Vector3, Vector3, c_float, c_float, c_int, Color)
draw_cylinder_wires_ex.restype = None

draw_capsule = raylib_dll.DrawCapsule
draw_capsule.argtypes = (Vector3, Vector3, c_float, c_int, c_int, Color)
draw_capsule.restype = None

draw_capsule_wires = raylib_dll.DrawCapsuleWires
draw_capsule_wires.argtypes = (Vector3, Vector3, c_float, c_int, c_int, Color)
draw_capsule_wires.restype = None

draw_plane = raylib_dll.DrawPlane
draw_plane.argtypes = (Vector3, Vector2, Color)
draw_plane.restype = None

draw_ray = raylib_dll.DrawRay
draw_ray.argtypes = (Ray, Color)
draw_ray.restype = None

draw_grid = raylib_dll.DrawGrid
draw_grid.argtypes = (c_int, c_float)
draw_grid.restype = None

# Model 3d Loading and Drawing Functions (Module: models)

# Model management functions
load_model = raylib_dll.LoadModel
load_model.argtypes = (c_char_p,)
load_model.restype = Model

load_model_from_mesh = raylib_dll.LoadModelFromMesh
load_model_from_mesh.argtypes = (Mesh,)
load_model_from_mesh.restype = Model

is_model_ready = raylib_dll.IsModelReady
is_model_ready.argtypes = (Model,)
is_model_ready.restype = c_bool

unload_model = raylib_dll.UnloadModel
unload_model.argtypes = (Model,)
unload_model.restype = None

get_model_bounding_box = raylib_dll.GetModelBoundingBox
get_model_bounding_box.argtypes = (Model,)
get_model_bounding_box.restype = BoundingBox

# Model drawing functions
draw_model = raylib_dll.DrawModel
draw_model.argtypes = (Model, Vector3, c_float, Color)
draw_model.restype = None

draw_model_ex = raylib_dll.DrawModelEx
draw_model_ex.argtypes = (Model, Vector3, Vector3, c_float, Vector3, Color)
draw_model_ex.restype = None

draw_model_wires = raylib_dll.DrawModelWires
draw_model_wires.argtypes = (Model, Vector3, c_float, Color)
draw_model_wires.restype = None

draw_model_wires_ex = raylib_dll.DrawModelWiresEx
draw_model_wires_ex.argtypes = (Model, Vector3, Vector3, c_float, Vector3, Color)
draw_model_wires_ex.restype = None

draw_bounding_box = raylib_dll.DrawBoundingBox
draw_bounding_box.argtypes = (BoundingBox, Color)
draw_bounding_box.restype = None

draw_billboard = raylib_dll.DrawBillboard
draw_billboard.argtypes = (Camera, Texture2D, Vector3, c_float, Color)
draw_billboard.restype = None

draw_billboard_rec = raylib_dll.DrawBillboardRec
draw_billboard_rec.argtypes = (Camera, Texture2D, Rectangle, Vector3, Vector2, Color)
draw_billboard_rec.restype = None

draw_billboard_pro = raylib_dll.DrawBillboardPro
draw_billboard_pro.argtypes = (Camera, Texture2D, Rectangle, Vector3, Vector3, Vector2, Vector2, c_float, Color)
draw_billboard_pro.restype = None

# Mesh management functions
upload_mesh = raylib_dll.UploadMesh
upload_mesh.argtypes = (ctypes.POINTER(Mesh), c_bool)
upload_mesh.restype = None

update_mesh_buffer = raylib_dll.UpdateMeshBuffer
update_mesh_buffer.argtypes = (Mesh, c_int, c_void_p, c_int, c_int)
update_mesh_buffer.restype = None

unload_mesh = raylib_dll.UnloadMesh
unload_mesh.argtypes = (Mesh,)
unload_mesh.restype = None

draw_mesh = raylib_dll.DrawMesh
draw_mesh.argtypes = (Mesh, Material, Matrix)
draw_mesh.restype = None

draw_mesh_instanced = raylib_dll.DrawMeshInstanced
draw_mesh_instanced.argtypes = (Mesh, Material, ctypes.POINTER(Matrix), c_int)
draw_mesh_instanced.restype = None

export_mesh = raylib_dll.ExportMesh
export_mesh.argtypes = (Mesh, c_char_p)
export_mesh.restype = c_bool

get_mesh_bounding_box = raylib_dll.GetMeshBoundingBox
get_mesh_bounding_box.argtypes = (Mesh,)
get_mesh_bounding_box.restype = BoundingBox

gen_mesh_tangents = raylib_dll.GenMeshTangents
gen_mesh_tangents.argtypes = (ctypes.POINTER(Mesh),)
gen_mesh_tangents.restype = None

# Mesh generation functions
gen_mesh_poly = raylib_dll.GenMeshPoly
gen_mesh_poly.argtypes = (c_int, c_float)
gen_mesh_poly.restype = Mesh

gen_mesh_plane = raylib_dll.GenMeshPlane
gen_mesh_plane.argtypes = (c_float, c_float, c_int, c_int)
gen_mesh_plane.restype = Mesh

gen_mesh_cube = raylib_dll.GenMeshCube
gen_mesh_cube.argtypes = (c_float, c_float, c_float)
gen_mesh_cube.restype = Mesh

gen_mesh_sphere = raylib_dll.GenMeshSphere
gen_mesh_sphere.argtypes = (c_float, c_int, c_int)
gen_mesh_sphere.restype = Mesh

gen_mesh_hemi_sphere = raylib_dll.GenMeshHemiSphere
gen_mesh_hemi_sphere.argtypes = (c_float, c_int, c_int)
gen_mesh_hemi_sphere.restype = Mesh

gen_mesh_cylinder = raylib_dll.GenMeshCylinder
gen_mesh_cylinder.argtypes = (c_float, c_float, c_int)
gen_mesh_cylinder.restype = Mesh

gen_mesh_cone = raylib_dll.GenMeshCone
gen_mesh_cone.argtypes = (c_float, c_float, c_int)
gen_mesh_cone.restype = Mesh

gen_mesh_torus = raylib_dll.GenMeshTorus
gen_mesh_torus.argtypes = (c_float, c_float, c_int, c_int)
gen_mesh_torus.restype = Mesh

gen_mesh_knot = raylib_dll.GenMeshKnot
gen_mesh_knot.argtypes = (c_float, c_float, c_int, c_int)
gen_mesh_knot.restype = Mesh

gen_mesh_heightmap = raylib_dll.GenMeshHeightmap
gen_mesh_heightmap.argtypes = (Image, Vector3)
gen_mesh_heightmap.restype = Mesh

gen_mesh_cubicmap = raylib_dll.GenMeshCubicmap
gen_mesh_cubicmap.argtypes = (Image, Vector3)
gen_mesh_cubicmap.restype = Mesh

# Material loading/unloading functions
load_materials = raylib_dll.LoadMaterials
load_materials.argtypes = (c_char_p, ctypes.POINTER(c_int))
load_materials.restype = ctypes.POINTER(Material)

load_material_default = raylib_dll.LoadMaterialDefault
load_material_default.argtypes = None
load_material_default.restype = Material

is_material_ready = raylib_dll.IsMaterialReady
is_material_ready.argtypes = (Material,)
is_material_ready.restype = c_bool

unload_material = raylib_dll.UnloadMaterial
unload_material.argtypes = (Material,)
unload_material.restype = None

set_material_texture = raylib_dll.SetMaterialTexture
set_material_texture.argtypes = (ctypes.POINTER(Material), c_int, Texture2D)
set_material_texture.restype = None

set_model_mesh_material = raylib_dll.SetModelMeshMaterial
set_model_mesh_material.argtypes = (ctypes.POINTER(Model), c_int, c_int)
set_model_mesh_material.restype = None

# Model animations loading/unloading functions
load_model_animations = raylib_dll.LoadModelAnimations
load_model_animations.argtypes = (c_char_p, ctypes.POINTER(c_int))
load_model_animations.restype = ctypes.POINTER(ModelAnimation)

update_model_animation = raylib_dll.UpdateModelAnimation
update_model_animation.argtypes = (Model, ModelAnimation, c_int)
update_model_animation.restype = None

unload_model_animation = raylib_dll.UnloadModelAnimation
unload_model_animation.argtypes = (ModelAnimation,)
unload_model_animation.restype = None

unload_model_animations = raylib_dll.UnloadModelAnimations
unload_model_animations.argtypes = (ctypes.POINTER(ModelAnimation), c_int)
unload_model_animations.restype = None

is_model_animation_valid = raylib_dll.IsModelAnimationValid
is_model_animation_valid.argtypes = (Model, ModelAnimation)
is_model_animation_valid.restype = c_bool

# Collision detection functions
check_collision_spheres = raylib_dll.CheckCollisionSpheres
check_collision_spheres.argtypes = (Vector3, c_float, Vector3, c_float)
check_collision_spheres.restype = c_bool

check_collision_boxes = raylib_dll.CheckCollisionBoxes
check_collision_boxes.argtypes = (BoundingBox, BoundingBox)
check_collision_boxes.restype = c_bool

check_collision_box_sphere = raylib_dll.CheckCollisionBoxSphere
check_collision_box_sphere.argtypes = (BoundingBox, Vector3, c_float)
check_collision_box_sphere.restype = c_bool

get_ray_collision_sphere = raylib_dll.GetRayCollisionSphere
get_ray_collision_sphere.argtypes = (Ray, Vector3, c_float)
get_ray_collision_sphere.restype = RayCollision

get_ray_collision_box = raylib_dll.GetRayCollisionBox
get_ray_collision_box.argtypes = (Ray, BoundingBox)
get_ray_collision_box.restype = RayCollision

get_ray_collision_mesh = raylib_dll.GetRayCollisionMesh
get_ray_collision_mesh.argtypes = (Ray, Mesh, Matrix)
get_ray_collision_mesh.restype = RayCollision

get_ray_collision_triangle = raylib_dll.GetRayCollisionTriangle
get_ray_collision_triangle.argtypes = (Ray, Vector3, Vector3, Vector3)
get_ray_collision_triangle.restype = RayCollision

get_ray_collision_quad = raylib_dll.GetRayCollisionQuad
get_ray_collision_quad.argtypes = (Ray, Vector3, Vector3, Vector3, Vector3)
get_ray_collision_quad.restype = RayCollision

# Audio Loading and Playing Functions (Module: audio)

AudioCallback = ctypes.CFUNCTYPE(None, c_void_p, c_uint)

# Audio device management functions
init_audio_device = raylib_dll.InitAudioDevice
init_audio_device.argtypes = None
init_audio_device.restype = None

close_audio_device = raylib_dll.CloseAudioDevice
close_audio_device.argtypes = None
close_audio_device.restype = None

is_audio_device_ready = raylib_dll.IsAudioDeviceReady
is_audio_device_ready.argtypes = None
is_audio_device_ready.restype = c_bool

set_master_volume = raylib_dll.SetMasterVolume
set_master_volume.argtypes = (c_float,)
set_master_volume.restype = None

get_master_volume = raylib_dll.GetMasterVolume
get_master_volume.argtypes = None
get_master_volume.restype = c_float

# Wave/Sound loading/unloading functions
load_wave = raylib_dll.LoadWave
load_wave.argtypes = (c_char_p,)
load_wave.restype = Wave

load_wave_from_memory = raylib_dll.LoadWaveFromMemory
load_wave_from_memory.argtypes = (c_char_p, ctypes.POINTER(c_ubyte), c_int)
load_wave_from_memory.restype = Wave

is_wave_ready = raylib_dll.IsWaveReady
is_wave_ready.argtypes = (Wave,)
is_wave_ready.restype = c_bool

load_sound = raylib_dll.LoadSound
load_sound.argtypes = (c_char_p,)
load_sound.restype = Sound

load_sound_from_wave = raylib_dll.LoadSoundFromWave
load_sound_from_wave.argtypes = (Wave,)
load_sound_from_wave.restype = Sound

load_sound_alias = raylib_dll.LoadSoundAlias
load_sound_alias.argtypes = (Sound,)
load_sound_alias.restype = Sound

is_sound_ready = raylib_dll.IsSoundReady
is_sound_ready.argtypes = (Sound,)
is_sound_ready.restype = c_bool

update_sound = raylib_dll.UpdateSound
update_sound.argtypes = (Sound, c_void_p, c_int)
update_sound.restype = None

unload_wave = raylib_dll.UnloadWave
unload_wave.argtypes = (Wave,)
unload_wave.restype = None

unload_sound = raylib_dll.UnloadSound
unload_sound.argtypes = (Sound,)
unload_sound.restype = None

unload_sound_alias = raylib_dll.UnloadSoundAlias
unload_sound_alias.argtypes = (Sound,)
unload_sound_alias.restype = None

export_wave = raylib_dll.ExportWave
export_wave.argtypes = (Wave, c_char_p)
export_wave.restype = c_bool

export_wave_as_code = raylib_dll.ExportWaveAsCode
export_wave_as_code.argtypes = (Wave, c_char_p)
export_wave_as_code.restype = c_bool

# Wave/Sound management functions
play_sound = raylib_dll.PlaySound
play_sound.argtypes = (Sound,)
play_sound.restype = None

stop_sound = raylib_dll.StopSound
stop_sound.argtypes = (Sound,)
stop_sound.restype = None

pause_sound = raylib_dll.PauseSound
pause_sound.argtypes = (Sound,)
pause_sound.restype = None

resume_sound = raylib_dll.ResumeSound
resume_sound.argtypes = (Sound,)
resume_sound.restype = None

is_sound_playing = raylib_dll.IsSoundPlaying
is_sound_playing.argtypes = (Sound,)
is_sound_playing.restype = c_bool

set_sound_volume = raylib_dll.SetSoundVolume
set_sound_volume.argtypes = (Sound, c_float)
set_sound_volume.restype = None

set_sound_pitch = raylib_dll.SetSoundPitch
set_sound_pitch.argtypes = (Sound, c_float)
set_sound_pitch.restype = None

set_sound_pan = raylib_dll.SetSoundPan
set_sound_pan.argtypes = (Sound, c_float)
set_sound_pan.restype = None

wave_copy = raylib_dll.WaveCopy
wave_copy.argtypes = (Wave,)
wave_copy.restype = Wave

wave_crop = raylib_dll.WaveCrop
wave_crop.argtypes = (ctypes.POINTER(Wave), c_int, c_int)
wave_crop.restype = None

wave_format = raylib_dll.WaveFormat
wave_format.argtypes = (ctypes.POINTER(Wave), c_int, c_int, c_int)
wave_format.restype = None

load_wave_samples = raylib_dll.LoadWaveSamples
load_wave_samples.argtypes = (Wave,)
load_wave_samples.restype = ctypes.POINTER(c_float)

unload_wave_samples = raylib_dll.UnloadWaveSamples
unload_wave_samples.argtypes = (ctypes.POINTER(c_float),)
unload_wave_samples.restype = None

# Music management functions
load_music_stream = raylib_dll.LoadMusicStream
load_music_stream.argtypes = (c_char_p,)
load_music_stream.restype = Music

load_music_stream_from_memory = raylib_dll.LoadMusicStreamFromMemory
load_music_stream_from_memory.argtypes = (c_char_p, ctypes.POINTER(c_ubyte), c_int)
load_music_stream_from_memory.restype = Music

is_music_ready = raylib_dll.IsMusicReady
is_music_ready.argtypes = (Music,)
is_music_ready.restype = c_bool

unload_music_stream = raylib_dll.UnloadMusicStream
unload_music_stream.argtypes = (Music,)
unload_music_stream.restype = None

play_music_stream = raylib_dll.PlayMusicStream
play_music_stream.argtypes = (Music,)
play_music_stream.restype = None

is_music_stream_playing = raylib_dll.IsMusicStreamPlaying
is_music_stream_playing.argtypes = (Music,)
is_music_stream_playing.restype = c_bool

update_music_stream = raylib_dll.UpdateMusicStream
update_music_stream.argtypes = (Music,)
update_music_stream.restype = None

stop_music_stream = raylib_dll.StopMusicStream
stop_music_stream.argtypes = (Music,)
stop_music_stream.restype = None

pause_music_stream = raylib_dll.PauseMusicStream
pause_music_stream.argtypes = (Music,)
pause_music_stream.restype = None

resume_music_stream = raylib_dll.ResumeMusicStream
resume_music_stream.argtypes = (Music,)
resume_music_stream.restype = None

seek_music_stream = raylib_dll.SeekMusicStream
seek_music_stream.argtypes = (Music, c_float)
seek_music_stream.restype = None

set_music_volume = raylib_dll.SetMusicVolume
set_music_volume.argtypes = (Music, c_float)
set_music_volume.restype = None

set_music_pitch = raylib_dll.SetMusicPitch
set_music_pitch.argtypes = (Music, c_float)
set_music_pitch.restype = None

set_music_pan = raylib_dll.SetMusicPan
set_music_pan.argtypes = (Music, c_float)
set_music_pan.restype = None

get_music_time_length = raylib_dll.GetMusicTimeLength
get_music_time_length.argtypes = (Music,)
get_music_time_length.restype = c_float

get_music_time_played = raylib_dll.GetMusicTimePlayed
get_music_time_played.argtypes = (Music,)
get_music_time_played.restype = c_float

# AudioStream management functions
load_audio_stream = raylib_dll.LoadAudioStream
load_audio_stream.argtypes = (c_uint, c_uint, c_uint)
load_audio_stream.restype = AudioStream

is_audio_stream_ready = raylib_dll.IsAudioStreamReady
is_audio_stream_ready.argtypes = (AudioStream,)
is_audio_stream_ready.restype = c_bool

unload_audio_stream = raylib_dll.UnloadAudioStream
unload_audio_stream.argtypes = (AudioStream,)
unload_audio_stream.restype = None

update_audio_stream = raylib_dll.UpdateAudioStream
update_audio_stream.argtypes = (AudioStream, c_void_p, c_int)
update_audio_stream.restype = None

is_audio_stream_processed = raylib_dll.IsAudioStreamProcessed
is_audio_stream_processed.argtypes = (AudioStream,)
is_audio_stream_processed.restype = c_bool

play_audio_stream = raylib_dll.PlayAudioStream
play_audio_stream.argtypes = (AudioStream,)
play_audio_stream.restype = None

pause_audio_stream = raylib_dll.PauseAudioStream
pause_audio_stream.argtypes = (AudioStream,)
pause_audio_stream.restype = None

resume_audio_stream = raylib_dll.ResumeAudioStream
resume_audio_stream.argtypes = (AudioStream,)
resume_audio_stream.restype = None

is_audio_stream_playing = raylib_dll.IsAudioStreamPlaying
is_audio_stream_playing.argtypes = (AudioStream,)
is_audio_stream_playing.restype = c_bool

stop_audio_stream = raylib_dll.StopAudioStream
stop_audio_stream.argtypes = (AudioStream,)
stop_audio_stream.restype = None

set_audio_stream_volume = raylib_dll.SetAudioStreamVolume
set_audio_stream_volume.argtypes = (AudioStream, c_float)
set_audio_stream_volume.restype = None

set_audio_stream_pitch = raylib_dll.SetAudioStreamPitch
set_audio_stream_pitch.argtypes = (AudioStream, c_float)
set_audio_stream_pitch.restype = None

set_audio_stream_pan = raylib_dll.SetAudioStreamPan
set_audio_stream_pan.argtypes = (AudioStream, c_float)
set_audio_stream_pan.restype = None

set_audio_stream_buffer_size_default = raylib_dll.SetAudioStreamBufferSizeDefault
set_audio_stream_buffer_size_default.argtypes = (c_int,)
set_audio_stream_buffer_size_default.restype = None

set_audio_stream_callback = raylib_dll.SetAudioStreamCallback
set_audio_stream_callback.argtypes = (AudioStream, AudioCallback)
set_audio_stream_callback.restype = None

attach_audio_stream_processor = raylib_dll.AttachAudioStreamProcessor
attach_audio_stream_processor.argtypes = (AudioStream, AudioCallback)
attach_audio_stream_processor.restype = None

detach_audio_stream_processor = raylib_dll.DetachAudioStreamProcessor
detach_audio_stream_processor.argtypes = (AudioStream, AudioCallback)
detach_audio_stream_processor.restype = None

attach_audio_mixed_processor = raylib_dll.AttachAudioMixedProcessor
attach_audio_mixed_processor.argtypes = (AudioCallback,)
attach_audio_mixed_processor.restype = None

detach_audio_mixed_processor = raylib_dll.DetachAudioMixedProcessor
detach_audio_mixed_processor.argtypes = (AudioCallback,)
detach_audio_mixed_processor.restype = None

camera_yaw = raylib_dll.CameraYaw
camera_yaw.argtypes = (ctypes.POINTER(Camera), c_float, c_bool)
camera_yaw.restype = None

camera_pitch = raylib_dll.CameraPitch
camera_pitch.argtypes = (ctypes.POINTER(Camera), c_float, c_bool, c_bool, c_bool)
camera_pitch.restype = None
