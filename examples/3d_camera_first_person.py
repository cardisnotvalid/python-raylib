from ctypes import pointer
from raylib import *

WINDOW_FACTOR = 100
WINDOW_WIDTH = 16 * WINDOW_FACTOR
WINDOW_HEIGHT = 9 * WINDOW_FACTOR
MAX_COLUMNS = 20

if __name__ == "__main__":
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, b"3d camera first person")

    camera = Camera3D(
        Vector3(10.0, 2.0, 4.0),
        Vector3(0.0, 2.0, 0.0),
        Vector3(0.0, 1.0, 0.0),
        60.0,
        CameraProjection.CAMERA_PERSPECTIVE,
    )

    camera_mode = CameraMode.CAMERA_FIRST_PERSON

    heights = []
    positions = []
    colors = []

    for i in range(MAX_COLUMNS):
        heights.append(get_random_value(1, 12))
        positions.append(Vector3(get_random_value(-15, 15), heights[i]/2.0,
                                 get_random_value(-15, 15)))
        colors.append(Color(get_random_value(20, 255),
                            get_random_value(10, 55), 30, 255))

    disable_cursor()
    set_target_fps(60)

    while not window_should_close():
        if is_key_pressed(KeyboardKey.KEY_ONE):
            camera_mode = CameraMode.CAMERA_FREE
            camera.up = Vector3(0.0, 1.0, 0.0)

        if is_key_pressed(KeyboardKey.KEY_TWO):
            camera_mode = CameraMode.CAMERA_FIRST_PERSON
            camera.up = Vector3(0.0, 1.0, 0.0)

        if is_key_pressed(KeyboardKey.KEY_THREE):
            camera_mode = CameraMode.CAMERA_THIRD_PERSON
            camera.up = Vector3(0.0, 1.0, 0.0)

        if is_key_pressed(KeyboardKey.KEY_FOUR):
            camera_mode = CameraMode.CAMERA_ORBITAL
            camera.up = Vector3(0.0, 1.0, 0.0)

        if is_key_pressed(KeyboardKey.KEY_P):
            if camera.projection == CameraProjection.CAMERA_PERSPECTIVE:
                camera.position = Vector3(0.0, 2.0, -100.0)
                camera.target = Vector3(0.0, 2.0, 0.0)
                camera.up = Vector3(0.0, 1.0, 0.0)
                camera.projection = CameraProjection.CAMERA_ORTHOGRAPHIC
                camera.fovy = 20.0
                camera_yaw(pointer(camera), -135 * (PI/180), True)
                camera_pitch(pointer(camera), -45 * (PI/180), True, True, False)
            else:
                camera.position = Vector3(0.0, 2.0, 10.0)
                camera.target = Vector3(0.0, 2.0, 0.0)
                camera.up = Vector3(0.0, 1.0, 0.0)
                camera.projection = CameraProjection.CAMERA_PERSPECTIVE
                camera.fovy = 60.0

        update_camera(pointer(camera), camera_mode)

        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode_3d(camera)
        draw_plane(Vector3(0.0, 0.0, 0.0), Vector2(32.0, 32.0), LIGHTGRAY)
        draw_cube(Vector3(-16.0, 2.5, 0.0), 1.0, 5.0, 32.0, DARKGRAY)
        draw_cube(Vector3(16.0, 2.5, 0.0), 1.0, 5.0, 32.0, DARKGRAY)
        draw_cube(Vector3(0.0, 2.5, 16.0), 32.0, 5.0, 1.0, DARKGRAY)
        draw_cube(Vector3(0.0, 2.5, -16.0), 32.0, 5.0, 1.0, DARKGRAY)

        for i in range(MAX_COLUMNS):
            draw_cube(positions[i], 2.0, heights[i], 2.0, colors[i])
            draw_cube_wires(positions[i], 2.0, heights[i], 2.0, MAROON)

        if camera_mode == CameraMode.CAMERA_THIRD_PERSON:
            draw_cube(camera.target, 0.5, 0.5, 0.5, PURPLE)
            draw_cube_wires(camera.target, 0.5, 0.5, 0.5, DARKPURPLE)
        end_mode_3d()

        draw_fps(0, 0)
        end_drawing()

    close_window()
