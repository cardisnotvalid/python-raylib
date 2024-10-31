from raylib import *

WINDOW_FACTOR = 100
WINDOW_WIDTH = 16 * WINDOW_FACTOR
WINDOW_HEIGHT = 9 * WINDOW_FACTOR

if __name__ == "__main__":
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, b"3d camera mode")

    camera = Camera3D(
        Vector3(0.0, 10.0, 10.0),
        Vector3(0.0, 0.0, 0.0),
        Vector3(0.0, 1.0, 0.0),
        45.0,
        CameraProjection.CAMERA_PERSPECTIVE,
    )

    cube_position = Vector3(0.0, 0.0, 0.0)

    disable_cursor()
    set_target_fps(60)

    while not window_should_close():
        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode_3d(camera)
        draw_cube(cube_position, 2.0, 2.0, 2.0, RED)
        draw_cube_wires(cube_position, 2.0, 2.0, 2.0, MAROON)
        draw_grid(10, 1.0)
        end_mode_3d()

        draw_text(b"Welcome to the third dimension!", 10, 40, 20, DARKGRAY)
        draw_fps(10, 10)

        end_drawing()

    close_window()
