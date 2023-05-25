import time
import usb_hid
from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

while True:
    x, y, z = cp.acceleration
    print ((x, y, z))
    if x > 3:
        kbd.send(Keycode.LEFT_ARROW)
    if x < -3:
        kbd.send(Keycode.RIGHT_ARROW)
    if cpx.button_a:
        kbd.send(Keycode.UP_ARROW)
    if cpx.button_b:
        kbd.send(Keycode.DOWN_ARROW)
    time.sleep(0.016666666667)

