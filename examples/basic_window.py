from raylib import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

if __name__ == "__main__":
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, b"basic window")

    set_target_fps(60)

    while not window_should_close():
        begin_drawing()
        clear_background(RAYWHITE)
        draw_text(b"Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)
        end_drawing()

    close_window()
