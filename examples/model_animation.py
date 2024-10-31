from ctypes import byref
from raylib import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

if __name__ == "__main__":
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, b"model animation")

    camera = Camera(
        Vector3(10.0, 10.0, 10.0),
        Vector3(0.0, 0.0, 0.0),
        Vector3(0.0, 1.0, 0.0),
        45.0,
        CameraProjection.CAMERA_PERSPECTIVE
    )

    model = load_model(b"resources/guy.iqm")
    texture = load_texture(b"resources/guytex.png")
    set_material_texture(byref(model.materials[0]), MaterialMapIndex.MATERIAL_MAP_DIFFUSE, texture)

    position = Vector3(0.0, 0.0, 0.0)

    anims_count = c_int(0)
    anims = load_model_animations(b"resources/guyanim.iqm", byref(anims_count))
    anim_frame_counter = 0

    disable_cursor()
    set_target_fps(60)

    while not window_should_close():
        update_camera(byref(camera), CameraMode.CAMERA_FIRST_PERSON)

        if is_key_down(KeyboardKey.KEY_SPACE):
            anim_frame_counter += 1
            update_model_animation(model, anims[0], anim_frame_counter)
            if anim_frame_counter >= anims[0].frameCount:
               anim_frame_counter = 0

        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode_3d(camera)
        draw_model_ex(model, position, Vector3(1.0, 0.0, 0.0), -90.0, Vector3(1.0, 1.0, 1.0), WHITE)

        for i in range(model.boneCount):
            draw_cube(anims[0].framePoses[anim_frame_counter][i].translation, 0.2, 0.2, 0.2, RED)

        draw_grid(10, 1.0)
        end_mode_3d()

        draw_text(b"PRESS SPACE to PLAY MODEL ANIMATION", 10, 10, 20, MAROON)
        draw_text(b"(c) Guy IQM 3D model by @culacant", WINDOW_WIDTH - 200, WINDOW_HEIGHT - 20, 10, GRAY)

        end_drawing()

    unload_texture(texture)
    unload_model_animations(anims, animsCount)
    unload_model(model)

    close_window()
