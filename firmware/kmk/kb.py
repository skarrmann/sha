import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14)
    row_pins = (board.GP28, board.GP4, board.GP27, board.GP5, board.GP26, board.GP6, board.GP15, board.GP7)
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.GP16
    rgb_num_pixels = 25

    coord_mapping = [
     0,  1,  2,  3,  4,  5,          8,  9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19,         22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33,         36, 37, 38, 39, 40, 41,
    42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55
    ]