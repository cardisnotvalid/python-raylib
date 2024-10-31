from raylib import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450
MAX_GESTURE_STRINGS = 20

if __name__ == "__main__":
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, b"input gestures")

    touch_position = Vector2(0.0, 0.0)
    touch_area = Rectangle(220.0, 10.0, WINDOW_WIDTH - 230.0, WINDOW_HEIGHT - 20.0)

    gestures_count = 0
    gesture_strings = [b"" for _ in range(MAX_GESTURE_STRINGS)]

    current_gesture = Gesture.GESTURE_NONE
    last_gesture = Gesture.GESTURE_NONE

    set_target_fps(60)

    while not window_should_close():
        last_gesture = current_gesture
        current_gesture = get_gesture_detected()
        touch_position = get_touch_position(0)

        if (
            check_collision_point_rec(touch_position, touch_area)
            and current_gesture != Gesture.GESTURE_NONE
        ):
            if current_gesture != last_gesture:
                if current_gesture == Gesture.GESTURE_TAP:
                    gesture_strings[gestures_count] = b"GESTURE TAP"
                elif current_gesture == Gesture.GESTURE_DOUBLETAP:
                    gesture_strings[gestures_count] = b"GESTURE DOUBLETAP"
                elif current_gesture == Gesture.GESTURE_HOLD:
                    gesture_strings[gestures_count] = b"GESTURE HOLD"
                elif current_gesture == Gesture.GESTURE_DRAG:
                    gesture_strings[gestures_count] = b"GESTURE DRAG"
                elif current_gesture == Gesture.GESTURE_SWIPE_RIGHT:
                    gesture_strings[gestures_count] = b"GESTURE SWIPE RIGHT"
                elif current_gesture == Gesture.GESTURE_SWIPE_LEFT:
                    gesture_strings[gestures_count] = b"GESTURE SWIPE LEFT"
                elif current_gesture == Gesture.GESTURE_SWIPE_UP:
                    gesture_strings[gestures_count] = b"GESTURE SWIPE UP"
                elif current_gesture == Gesture.GESTURE_SWIPE_DOWN:
                    gesture_strings[gestures_count] = b"GESTURE SWIPE DOWN"
                elif current_gesture == Gesture.GESTURE_PINCH_IN:
                    gesture_strings[gestures_count] = b"GESTURE PINCH IN"
                elif current_gesture == Gesture.GESTURE_PINCH_OUT:
                    gesture_strings[gestures_count] = b"GESTURE PINCH OUT"

                gestures_count += 1

                if gestures_count >= MAX_GESTURE_STRINGS:
                    for i in range(MAX_GESTURE_STRINGS):
                        gesture_strings = [b"" for _ in range(MAX_GESTURE_STRINGS)]
                        gestures_count = 0

        begin_drawing()
        clear_background(RAYWHITE)

        draw_rectangle_rec(touch_area, GRAY)
        draw_rectangle(225, 15, WINDOW_WIDTH - 240, WINDOW_HEIGHT - 30, RAYWHITE)

        draw_text(b"GESTURES TEST AREA", WINDOW_WIDTH - 270, WINDOW_HEIGHT - 40, 20, fade(GRAY, 0.5))

        for i in range(gestures_count):
            if i % 2 == 0:
                draw_rectangle(10, 30 + 20 * i, 200, 20, fade(LIGHTGRAY, 0.5))
            else:
                draw_rectangle(10, 30 + 20 * i, 200, 20, fade(LIGHTGRAY, 0.3))

            if i < gestures_count - 1:
                draw_text(gesture_strings[i], 35, 36 + 20 * i, 10, DARKGRAY)
            else:
                draw_text(gesture_strings[i], 35, 36 + 20 * i, 10, MAROON)

        draw_rectangle_lines(10, 29, 200, WINDOW_HEIGHT - 50, GRAY)
        draw_text(b"DETECTED GESTURES", 50, 15, 10, GRAY)

        if current_gesture != Gesture.GESTURE_NONE:
            draw_circle_v(touch_position, 30, MAROON)

        end_drawing()

    close_window()
