from enum import Enum
from utils import number_to_words
from pynput.keyboard import Key

class Command(Enum):
    """
    Commands to shortcut mappings for keyboard.send
    """

    DO_NOTHING = {"key" : "", "modifiers" : []}

    # Numbers and Symbols
    ZERO = {"key" : "0", "modifiers" : []}
    ONE = {"key" : "1", "modifiers" : []}
    TWO = {"key" : "2", "modifiers" : []}
    THREE = {"key" : "3", "modifiers" : []}
    FOUR = {"key" : "4", "modifiers" : []}
    FIVE = {"key" : "5", "modifiers" : []}
    SIX = {"key" : "6", "modifiers" : []}
    SEVEN = {"key" : "7", "modifiers" : []}
    EIGHT = {"key" : "8", "modifiers" : []}
    NINE = {"key" : "9", "modifiers" : []}
    DECIMAL = {"key" : ".", "modifiers" : []}
    MINUS = {"key" : "-", "modifiers" : []}
    PLUS = {"key" : "+", "modifiers" : []}
    PLUS_PERCENT = {"key" : "+", "modifiers" : [Key.shift]}
    MINUS_PERCENT = {"key" : "-", "modifiers" : [Key.shift]}
    DIVIDE = {"key" : "/", "modifiers" : []}

    # Console Modes
    LIVE = {"key" : "", "modifiers" : [Key.f1]}
    BLIND = {"key" : "", "modifiers" : [Key.f2]}
    STAGING = {"key" : "", "modifiers" : [Key.f6]}

    # Common Commands
    CUE = {"key" : "q", "modifiers" : []}
    AT = {"key" : "@", "modifiers" : []}
    OUT = {"key" : "o", "modifiers" : []}
    THRU = {"key" : "t", "modifiers" : []}
    UPDATE = {"key" : "u", "modifiers" : []}
    GROUP = {"key" : "g", "modifiers" : []}
    ENTER = {"key" : "", "modifiers" : [Key.enter]}
    GOTOCUE = {"key" : "g", "modifiers" : [Key.ctrl]}
    FULL = {"key" : "f", "modifiers" : []}
    CLEAR = {"key" : "", "modifiers" : [Key.backspace]}
    SHIFT_CLEAR = {"key" : "", "modifiers" : [Key.shift, Key.backspace]}
    DELETE = {"key" : "", "modifiers" : [Key.delete]}
    GO = {"key" : "", "modifiers" : []}
    HOME = {"key" : "", "modifiers" : [Key.home]}
    MARK = {"key" : "k", "modifiers" : []}
    RECALLFROM = {"key" : "e", "modifiers" : []}
    SHIFT = {"key" : "z", "modifiers" : []}
    SNEAK = {"key" : "n", "modifiers" : []}
    PATCH = {"key" : ";", "modifiers" : []}
    RECORD = {"key" : "r", "modifiers" : []}
    RECORD_ONLY = {"key" : "r", "modifiers" : [Key.ctrl]}
    UNDO = {"key" : "x", "modifiers" : [Key.ctrl]}

    # Navigation and Camera
    NEXT = {"key": "", "modifiers": [Key.page_down]}
    LAST = {"key": "", "modifiers": [Key.page_up]}
    CAMERA_UP = {"key": "", "modifiers": [Key.up]}
    CAMERA_DOWN = {"key": "", "modifiers": [Key.down]}
    CAMERA_LEFT = {"key": "", "modifiers": [Key.left]}
    CAMERA_RIGHT = {"key": "", "modifiers": [Key.right]}
    CAMERA_FORWARDS = {"key": "", "modifiers": [Key.shift, Key.up]}
    CAMERA_BACKWARDS = {"key": "", "modifiers": [Key.shift, Key.down]}
    CAMERA_UP_EDIT = {"key": "w", "modifiers": []}
    CAMERA_DOWN_EDIT = {"key": "s", "modifiers": []}
    CAMERA_LEFT_EDIT = {"key": "a", "modifiers": []}
    CAMERA_RIGHT_EDIT = {"key": "d", "modifiers": []}
    CAMERA_FORWARDS_EDIT = {"key": "w", "modifiers": [Key.shift]}
    CAMERA_BACKWARDS_EDIT = {"key": "s", "modifiers": [Key.shift]}

    # System Controls
    ESCAPE = {"key": "", "modifiers": [Key.esc]}
    TAB = {"key": "", "modifiers": [Key.tab]}
    EXPAND = {"key": "", "modifiers": [Key.f5]}
    FLEXI_CHANNEL = {"key": "", "modifiers": [Key.f3]}
    DISPLAYS = {"key": "", "modifiers": [Key.f9]}
    TOGGLE_HOTKEYS = {"key": "", "modifiers": [Key.f8]}

    # Softkeys and Submaster
    SOFTKEY_1 = {"key": "1", "modifiers": [Key.alt]}
    SOFTKEY_2 = {"key": "2", "modifiers": [Key.alt]}
    SOFTKEY_3 = {"key": "3", "modifiers": [Key.alt]}
    SOFTKEY_4 = {"key": "4", "modifiers": [Key.alt]}
    SOFTKEY_5 = {"key": "5", "modifiers": [Key.alt]}
    SOFTKEY_6 = {"key": "6", "modifiers": [Key.alt]}
    SUBMASTER = {"key": "s", "modifiers": []}

    # Miscellaneous
    LABEL = {"key": "l", "modifiers": []}
    PART = {"key": "p", "modifiers": []}
    INTENSITY_FILTER = {"key": "i", "modifiers": [Key.ctrl]}
    COLOR_FILTER = {"key": "c", "modifiers": [Key.ctrl]}
    EFFECT = {"key": "e", "modifiers": [Key.alt]}
    SNAPSHOT = {"key": "s", "modifiers": [Key.ctrl]}
    TIME = {"key": "i", "modifiers": []}
    TIME_DISPLAY = {"key": "i", "modifiers": [Key.ctrl, Key.alt]}
    RATE = {"key": "r", "modifiers": [Key.ctrl, Key.alt]}
    OFFSET = {"key": "o", "modifiers": [Key.ctrl]}
    QUERY = {"key": "q", "modifiers": [Key.ctrl]}
    PARK = {"key": "k", "modifiers": [Key.alt]}
    STOP_EFFECT = {"key": "e", "modifiers": [Key.shift, Key.alt]}
    MAGIC_SHEET = {"key": "m", "modifiers": [Key.alt]}
    MACRO_801 = {"key": "1", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_802 = {"key": "2", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_803 = {"key": "3", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_804 = {"key": "4", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_805 = {"key": "5", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_806 = {"key": "6", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_807 = {"key": "7", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_808 = {"key": "8", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_809 = {"key": "9", "modifiers": [Key.ctrl, Key.alt]}
    MACRO_810 = {"key": "0", "modifiers": [Key.ctrl, Key.alt]}


words_to_commands = {
    "live": Command.LIVE,
    "blind": Command.BLIND,
    "staging": Command.STAGING,
    "zero": Command.ZERO,
    "one": Command.ONE,
    "two": Command.TWO,
    "three": Command.THREE,
    "four": Command.FOUR,
    "five": Command.FIVE,
    "six": Command.SIX,
    "seven": Command.SEVEN,
    "eight": Command.EIGHT,
    "nine": Command.NINE,

    "point": Command.DECIMAL,
    "minus": Command.MINUS,
    "plus": Command.PLUS,
    "slash": Command.DIVIDE,

    "cue": Command.CUE,
    "at": Command.AT,
    "out": Command.OUT,
    "thru": Command.THRU,
    "update": Command.UPDATE,
    "group": Command.GROUP,
    "enter": Command.ENTER,
    "go to cue": Command.GOTOCUE,
    "full": Command.FULL,
    "clear": Command.CLEAR,
    "shift clear": Command.SHIFT_CLEAR,
    "delete": Command.DELETE,
    "go": Command.GO,
    "home": Command.HOME,
    "mark": Command.MARK,
    "recall from": Command.RECALLFROM,
    "shift": Command.SHIFT,
    "sneak": Command.SNEAK,
    "patch": Command.PATCH,
    "record": Command.RECORD,
    "record only": Command.RECORD_ONLY,
    "undo": Command.UNDO,
    "next": Command.NEXT,
    "last": Command.LAST,
    "camera up": Command.CAMERA_UP,
    "camera down": Command.CAMERA_DOWN,
    "camera left": Command.CAMERA_LEFT,
    "camera right": Command.CAMERA_RIGHT,
    "camera forwards": Command.CAMERA_FORWARDS,
    "camera backwards": Command.CAMERA_BACKWARDS,
    "camera up edit": Command.CAMERA_UP_EDIT,
    "camera down edit": Command.CAMERA_DOWN_EDIT,
    "camera left edit": Command.CAMERA_LEFT_EDIT,
    "camera right edit": Command.CAMERA_RIGHT_EDIT,
    "camera forwards edit": Command.CAMERA_FORWARDS_EDIT,
    "camera backwards edit": Command.CAMERA_BACKWARDS_EDIT,
    "escape": Command.ESCAPE,
    "tab": Command.TAB,
    "expand": Command.EXPAND,
    "flexichannel": Command.FLEXI_CHANNEL,
    "displays": Command.DISPLAYS,
    "toggle hotkeys": Command.TOGGLE_HOTKEYS,
    "softkey one": Command.SOFTKEY_1,
    "softkey two": Command.SOFTKEY_2,
    "softkey three": Command.SOFTKEY_3,
    "softkey four": Command.SOFTKEY_4,
    "softkey five": Command.SOFTKEY_5,
    "softkey six": Command.SOFTKEY_6,
    "submaster": Command.SUBMASTER,
    "label": Command.LABEL,
    "part": Command.PART,
    "intensity filter": Command.INTENSITY_FILTER,
    "color filter": Command.COLOR_FILTER,
    "effect": Command.EFFECT,
    "snapshot": Command.SNAPSHOT,
    "time": Command.TIME,
    "time display": Command.TIME_DISPLAY,
    "rate": Command.RATE,
    "offset": Command.OFFSET,
    "query": Command.QUERY,
    "park": Command.PARK,
    "stop effect": Command.STOP_EFFECT,
    "magic sheet": Command.MAGIC_SHEET,
    "macro eight oh one": Command.MACRO_801,
    "macro eight hundred one": Command.MACRO_801,
    "macro eight hundred and one": Command.MACRO_801,
    "macro eight oh two": Command.MACRO_802,
    "macro eight hundred two": Command.MACRO_802,
    "macro eight hundred and two": Command.MACRO_802,
    "macro eight oh three": Command.MACRO_803,
    "macro eight hundred three": Command.MACRO_803,
    "macro eight hundred and three": Command.MACRO_803,
    "macro eight oh four": Command.MACRO_804,
    "macro eight hundred four": Command.MACRO_804,
    "macro eight hundred and four": Command.MACRO_804,
    "macro eight oh five": Command.MACRO_805,
    "macro eight hundred five": Command.MACRO_805,
    "macro eight hundred and five": Command.MACRO_805,
    "macro eight oh six": Command.MACRO_806,
    "macro eight hundred six": Command.MACRO_806,
    "macro eight hundred and six": Command.MACRO_806,
    "macro eight oh seven": Command.MACRO_807,
    "macro eight hundred seven": Command.MACRO_807,
    "macro eight hundred and seven": Command.MACRO_807,
    "macro eight oh eight": Command.MACRO_808,
    "macro eight hundred eight": Command.MACRO_808,
    "macro eight hundred and eight": Command.MACRO_808,
    "macro eight oh nine": Command.MACRO_809,
    "macro eight hundred nine": Command.MACRO_809,
    "macro eight hundred and nine": Command.MACRO_809,
    "macro eight ten": Command.MACRO_810,
    "macro eight hundred ten": Command.MACRO_810,
    "macro eight hundred and ten": Command.MACRO_810,


    # Common words that shouldn't do anything
    # These are often used colloquially but don't have a direct command mapping
    "channel": Command.DO_NOTHING,
    "channels": Command.DO_NOTHING,
    "light": Command.DO_NOTHING,
    "lights": Command.DO_NOTHING,

}



number_words = [number_to_words(i) for i in range(1001)]
