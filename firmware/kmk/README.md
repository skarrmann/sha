# Sha KMK Firmware

## Installation instructions

Apply these steps for either the RP2040-Zero or RP2040-Matrix:

1. Install CircuitPython:
    * https://circuitpython.org/board/waveshare_rp2040_zero/
2. Copy KMK firmware files:
    * https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md
3. Copy the custom files:
    * [`kb.py`](kb.py)
    * [`main.py`](main.py)

Now customize the layout and features in [`main.py`](main.py) file, and save the updates on your board.

Currently, the layout does not use the RGB LEDs of the RP2040-Matrix. Using [KMK's RGB extension](http://kmkfw.io/docs/rgb), I could not get the LEDs to properly respond (they would only light up fully blue, red, or green). I will investigate and resolve this as time permits.

## Default keymap

The default keymap is my personal layout, used on both Sha and Horizon.

Keyboard layout editor URL: http://www.keyboard-layout-editor.com/#/gists/a50829674ed7be41396659aaf38d1ddb