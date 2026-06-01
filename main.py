dice = 0

def on_gesture_shake():
    global dice
    dice = randint(1, 6)
    if dice == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif dice == 2:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            """)
    elif dice == 3:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . #
            """)
    elif dice == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif dice == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
