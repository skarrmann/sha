from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB


keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
rgb = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=keyboard.rgb_num_pixels,
    val_default=1,
    val_step=1,
    val_limit=8
    )
keyboard.extensions.append(rgb)

SYMTAB = KC.LT(1, KC.TAB, prefer_hold=True, tap_interrupted=True, tap_time=130)
FUNSPC = KC.LT(2, KC.SPC, prefer_hold=True, tap_interrupted=True, tap_time=180)

keyboard.keymap = [
    [   # Default (Colemak)
        KC.SCLN, KC.Q,    KC.W,    KC.F,    KC.P,    KC.G,                      KC.J,    KC.L,    KC.U,    KC.Y,    KC.QUOT, KC.MINS,
        KC.LSFT, KC.A,    KC.R,    KC.S,    KC.T,    KC.D,                      KC.H,    KC.N,    KC.E,    KC.I,    KC.O,    KC.RSFT,
        KC.LCTL, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                      KC.K,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RCTL,
        KC.LALT, KC.LGUI, KC.NO,   KC.NO,   KC.DEL,  SYMTAB,  KC.ESC,  KC.ENT,  FUNSPC,  KC.BSPC, KC.NO,   KC.NO,   KC.RGUI, KC.RALT
    ],
    [   # Symbol
        KC.COLN, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                     KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.DQUO, KC.UNDS,
        KC.HASH, KC.EXLM, KC.LPRN, KC.RPRN, KC.DLR,  KC.AMPR,                   KC.PIPE, KC.EQL,  KC.LCBR, KC.RCBR, KC.N0,   KC.GRV,
        KC.TILD, KC.AT,   KC.LBRC, KC.RBRC, KC.PLUS, KC.PERC,                   KC.CIRC, KC.ASTR, KC.LABK, KC.RABK, KC.QUES, KC.BSLS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.SPC,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],
    [   # Function
        KC.TRNS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.PSCR,                   KC.SLCK, KC.HOME, KC.PGDN, KC.PGUP, KC.END,  KC.TRNS,
        KC.TRNS, KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.INS,                    KC.CAPS, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.TRNS,
        KC.TRNS, KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.APP,                    KC.NLCK, KC.MUTE, KC.VOLD, KC.VOLU, KC.PAUS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TAB,  KC.TRNS, KC.TRNS, KC.SPC,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ]
]


if __name__ == '__main__':
    keyboard.go()
