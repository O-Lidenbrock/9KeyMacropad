# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
col_pins = [board.D5, board.D6, board.D7]
row_pins = [board.D8, board.D9, board.D10, board.D11]
diode_orientation = DiodeOrientation.COL2ROW 

keyboard.keymap = [
    KC.ONE, KC.NO, KC.TWO,
    KC.THREE, KC.FOUR, KC.FIVE,
    KC.SIX, KC.SEVEN, KC.EIGHT,
    KC.NINE, KC.ZERO, KC.A,
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()