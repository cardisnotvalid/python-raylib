from raylib import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450
MAX_FRAME_SPEED = 15
MIN_FRAME_SPEED = 1

if __name__ == "__main__":
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, b"sprite animation")

    scarfy = load_texture(b"resources/scarfy.png")

    position = Vector2(350.0, 280.0)
    frame_rec = Rectangle(0.0, 0.0, float(scarfy.width) / 6, float(scarfy.height))
    current_frame = 0
    
    frames_counter = 0
    frames_speed = 8

    set_target_fps(60)

    while not window_should_close():
        frames_counter += 1

        if frames_counter >= (60 / frames_speed):
            frames_counter = 0
            current_frame += 1

            if current_frame > 5:
                current_frame = 0

            frame_rec.x = float(current_frame) * float(scarfy.width) / 6

        if is_key_pressed(KeyboardKey.KEY_RIGHT):
            frames_speed += 1
        elif is_key_pressed(KeyboardKey.KEY_LEFT):
            frames_speed -= 1

        if frames_speed > MAX_FRAME_SPEED:
            frames_speed = MAX_FRAME_SPEED
        elif frames_speed < MIN_FRAME_SPEED:
            frames_speed = MIN_FRAME_SPEED

        begin_drawing()
        clear_background(RAYWHITE)

        draw_texture(scarfy, 15, 40, WHITE)
        draw_rectangle_lines(15, 40, scarfy.width, scarfy.height, LIME)
        draw_rectangle_lines(15 + int(frame_rec.x), 40 + int(frame_rec.y), int(scarfy.width / 6), int(scarfy.height), RED)

        draw_text(b"FRAME SPEED: ", 165, 210, 10, DARKGRAY)
        draw_text(b"%02i" % frames_speed, 575, 210, 10, DARKGRAY)
        draw_text(b"PRESS RIGHT/LEFT KEYS to CHANGE SPEED", 290, 240, 10, DARKGRAY)

        for i in range(MAX_FRAME_SPEED):
            if i < frames_speed:
                draw_rectangle(250 + 21 * i, 205, 20, 20, RED)
            draw_rectangle_lines(250 + 21 * i, 205, 20, 20, MAROON)

        draw_texture_rec(scarfy, frame_rec, position, WHITE)
        draw_text(b"(c) Scarfy sprite by Eiden Marsal", WINDOW_WIDTH - 200, WINDOW_HEIGHT - 20, 10 ,GRAY)

        end_drawing()

    unload_texture(scarfy)

    close_window()
