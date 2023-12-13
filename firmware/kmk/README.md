# Sha KMK Firmware

## Installation instructions

Apply these steps for the RP2040-Zero or RP-2040 Matrix:

1. Install CircuitPython:
    * https://circuitpython.org/board/waveshare_rp2040_zero/
2. Copy KMK firmware files:
    * https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md
3. Copy the custom files:
    * [`kb.py`](kb.py)
    * [`main.py`](main.py)

Now customize the layout and features in [`main.py`](main.py) file, and save the updates on your board.

The default layout uses KMK's RGB extension, and assigns the LEDs for the RP2040-Matrix. If using the RGB feature, you will also need to install the NeoPixel library from Adafruit. Refer to the [KMK RGB documentation](http://kmkfw.io/docs/rgb#circuitpython).

## Default keymap

The default keymap is my personal layout, used on both Sha and Horizon.

Keyboard layout editor URL: http://www.keyboard-layout-editor.com/#/gists/a50829674ed7be41396659aaf38d1ddb