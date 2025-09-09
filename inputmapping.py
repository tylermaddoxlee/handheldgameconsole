#!/usr/bin/env python3
import uinput
from gpiozero import Button
import signal

# Mapping: GPIO pin -> keyboard key
BUTTONS = {
    19: uinput.KEY_W,       # D-PAD UP
    5:  uinput.KEY_S,       # D-PAD DOWN
    13: uinput.KEY_A,       # D-PAD LEFT
    6:  uinput.KEY_D,       # D-PAD RIGHT
    26: uinput.KEY_ENTER,   # START
    10: uinput.KEY_RIGHTSHIFT, # SELECT
    20: uinput.KEY_H,       # BUTTON A
    21: uinput.KEY_G,       # BUTTON B
    12: uinput.KEY_T,       # BUTTON X
    16: uinput.KEY_F,       # BUTTON Y
    9:  uinput.KEY_Q,       # LEFT SHOULDER
    8:  uinput.KEY_E,       # RIGHT SHOULDER
    11: uinput.KEY_Z,       # LEFT TRIGGER
    7:  uinput.KEY_C        # RIGHT TRIGGER
}

# Create a virtual input device with all keys
device = uinput.Device(list(BUTTONS.values()))

# Setup GPIO buttons
buttons = {pin: Button(pin, pull_up=True) for pin in BUTTONS}

# Define press/release handlers
def press(key):
    device.emit(key, 1)  # Press

def release(key):
    device.emit(key, 0)  # Release

# Attach handlers
for pin, btn in buttons.items():
    btn.when_pressed = lambda pin=pin: press(BUTTONS[pin])
    btn.when_released = lambda pin=pin: release(BUTTONS[pin])

print("GPIO Gamepad running... Press Ctrl+C to exit.")
signal.pause()
