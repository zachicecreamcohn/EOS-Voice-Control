from enum import Enum
from utils import number_to_words
from pynput.keyboard import Key

class Command(Enum):
    """
    Commands to shortcut mappings for keyboard.send
    """

    DO_NOTHING = {"key" : "", "modifiers" : []}

    # Numbers and Symbols
    ZERO = {"shortcut": {"key" : "0", "modifiers" : []}, "OSC": {"commands":[]}}
    ONE = {"shortcut": {"key" : "1", "modifiers" : []}, "OSC": {"commands":[]}}
    TWO = {"shortcut": {"key" : "2", "modifiers" : []}, "OSC": {"commands":[]}}
    THREE = {"shortcut": {"key" : "3", "modifiers" : []}, "OSC": {"commands":[]}}
    FOUR = {"shortcut": {"key" : "4", "modifiers" : []}, "OSC": {"commands":[]}}
    FIVE = {"shortcut": {"key" : "5", "modifiers" : []}, "OSC": {"commands":[]}}
    SIX = {"shortcut": {"key" : "6", "modifiers" : []}, "OSC": {"commands":[]}}
    SEVEN = {"shortcut": {"key" : "7", "modifiers" : []}, "OSC": {"commands":[]}}
    EIGHT = {"shortcut": {"key" : "8", "modifiers" : []}, "OSC": {"commands":[]}}
    NINE = {"shortcut": {"key" : "9", "modifiers" : []}, "OSC": {"commands":[]}}
    DECIMAL = {"shortcut": {"key" : ".", "modifiers" : []}, "OSC": {"commands":[]}}
    MINUS = {"shortcut": {"key" : "-", "modifiers" : []}, "OSC": {"commands":[]}}
    PLUS = {"shortcut": {"key" : "+", "modifiers" : []}, "OSC": {"commands":[]}}
    PLUS_PERCENT = {"shortcut": {"key" : "+", "modifiers" : [Key.shift]}, "OSC": {"commands":[]}}
    MINUS_PERCENT = {"shortcut": {"key" : "-", "modifiers" : [Key.shift]}, "OSC": {"commands":[]}}
    DIVIDE = {"shortcut": {"key" : "/", "modifiers" : []}, "OSC": {"commands":[]}}

    # Console Modes
    LIVE = {"shortcut": {"key" : "", "modifiers" : [Key.f1]}, "OSC": {"commands":[]}}
    BLIND = {"shortcut": {"key" : "", "modifiers" : [Key.f2]}, "OSC": {"commands":[]}}
    STAGING = {"shortcut": {"key" : "", "modifiers" : [Key.f6]}, "OSC": {"commands":[]}}

    # Common Commands
    CUE = {"shortcut": {"key" : "q", "modifiers" : []}, "OSC": {"commands":[]}}
    AT = {"shortcut": {"key" : "a", "modifiers" : []}, "OSC": {"commands":[]}}
    ATAT = {"shortcut": {"key" : "aa", "modifiers" : []}, "OSC": {"commands":[]}}
    OUT = {"shortcut": {"key" : "o", "modifiers" : []}, "OSC": {"commands":[]}}
    THRU = {"shortcut": {"key" : "t", "modifiers" : []}, "OSC": {"commands":[]}}
    UPDATE = {"shortcut": {"key" : "u", "modifiers" : []}, "OSC": {"commands":[]}}
    GROUP = {"shortcut": {"key" : "g", "modifiers" : []}, "OSC": {"commands":[]}}
    ENTER = {"shortcut": {"key" : "", "modifiers" : [Key.enter]}, "OSC": {"commands":[]}}
    GOTOCUE = {"shortcut": {"key" : "g", "modifiers" : [Key.ctrl]}, "OSC": {"commands":[]}}
    FULL = {"shortcut": {"key" : "f", "modifiers" : []}, "OSC": {"commands":[]}}
    CLEAR = {"shortcut": {"key" : "", "modifiers" : [Key.backspace]}, "OSC": {"commands":[]}}
    SHIFT_CLEAR = {"shortcut": {"key" : "", "modifiers" : [Key.shift, Key.backspace]}, "OSC": {"commands":[]}}
    DELETE = {"shortcut": {"key" : "", "modifiers" : [Key.delete]}, "OSC": {"commands":[]}}
    GO = {"shortcut": {"key" : " ", "modifiers" : []}, "OSC": {"commands":[]}}
    STOP_BACK = {"shortcut": {"key" : " ", "modifiers" : [Key.ctrl]}, "OSC": {"commands":[]}}
    HOME = {"shortcut": {"key" : "", "modifiers" : [Key.home]}, "OSC": {"commands":[]}}
    MARK = {"shortcut": {"key" : "k", "modifiers" : []}, "OSC": {"commands":[]}}
    RECALLFROM = {"shortcut": {"key" : "e", "modifiers" : []}, "OSC": {"commands":[]}}
    SHIFT = {"shortcut": {"key" : "z", "modifiers" : []}, "OSC": {"commands":[]}}
    SNEAK = {"shortcut": {"key" : "n", "modifiers" : []}, "OSC": {"commands":[]}}
    PATCH = {"shortcut": {"key" : ";", "modifiers" : []}, "OSC": {"commands":[]}}
    RECORD = {"shortcut": {"key" : "r", "modifiers" : []}, "OSC": {"commands":[]}}
    RECORD_ONLY = {"shortcut": {"key" : "r", "modifiers" : [Key.ctrl]}, "OSC": {"commands":[]}}
    UNDO = {"shortcut": {"key" : "x", "modifiers" : [Key.ctrl]}, "OSC": {"commands":[]}}
    FOLLOW = {"shortcut": {"key" : "d", "modifiers" : [Key.shift]}, "OSC": {"commands":[]}}
    HANG = {"shortcut": {"key" : "dd", "modifiers" : [Key.shift]}, "OSC": {"commands":[]}}

    # Navigation and Camera
    NEXT = {"shortcut": {"key": "", "modifiers": [Key.page_down]}, "OSC": {"commands":[]}}
    LAST = {"shortcut": {"key": "", "modifiers": [Key.page_up]}, "OSC": {"commands":[]}}
    CAMERA_UP = {"shortcut": {"key": "", "modifiers": [Key.up]}, "OSC": {"commands":[]}}
    CAMERA_DOWN = {"shortcut": {"key": "", "modifiers": [Key.down]}, "OSC": {"commands":[]}}
    CAMERA_LEFT = {"shortcut": {"key": "", "modifiers": [Key.left]}, "OSC": {"commands":[]}}
    CAMERA_RIGHT = {"shortcut": {"key": "", "modifiers": [Key.right]}, "OSC": {"commands":[]}}
    CAMERA_FORWARDS = {"shortcut": {"key": "", "modifiers": [Key.shift, Key.up]}, "OSC": {"commands":[]}}
    CAMERA_BACKWARDS = {"shortcut": {"key": "", "modifiers": [Key.shift, Key.down]}, "OSC": {"commands":[]}}
    CAMERA_UP_EDIT = {"shortcut": {"key": "w", "modifiers": []}, "OSC": {"commands":[]}}
    CAMERA_DOWN_EDIT = {"shortcut": {"key": "s", "modifiers": []}, "OSC": {"commands":[]}}
    CAMERA_LEFT_EDIT = {"shortcut": {"key": "a", "modifiers": []}, "OSC": {"commands":[]}}
    CAMERA_RIGHT_EDIT = {"shortcut": {"key": "d", "modifiers": []}, "OSC": {"commands":[]}}
    CAMERA_FORWARDS_EDIT = {"shortcut": {"key": "w", "modifiers": [Key.shift]}, "OSC": {"commands":[]}}
    CAMERA_BACKWARDS_EDIT = {"shortcut": {"key": "s", "modifiers": [Key.shift]}, "OSC": {"commands":[]}}

    # System Controls
    ESCAPE = {"shortcut": {"key": "", "modifiers": [Key.esc]}, "OSC": {"commands":[]}}
    TAB = {"shortcut": {"key": "", "modifiers": [Key.tab]}, "OSC": {"commands":[]}}
    EXPAND = {"shortcut": {"key": "", "modifiers": [Key.f5]}, "OSC": {"commands":[]}}
    FLEXI_CHANNEL = {"shortcut": {"key": "", "modifiers": [Key.f3]}, "OSC": {"commands":[]}}
    DISPLAYS = {"shortcut": {"key": "", "modifiers": [Key.f9]}, "OSC": {"commands":[]}}
    TOGGLE_HOTKEYS = {"shortcut": {"key": "", "modifiers": [Key.f8]}, "OSC": {"commands":[]}}

    # Softkeys and Submaster
    SOFTKEY_1 = {"shortcut": {"key": "1", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    SOFTKEY_2 = {"shortcut": {"key": "2", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    SOFTKEY_3 = {"shortcut": {"key": "3", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    SOFTKEY_4 = {"shortcut": {"key": "4", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    SOFTKEY_5 = {"shortcut": {"key": "5", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    SOFTKEY_6 = {"shortcut": {"key": "6", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    SUBMASTER = {"shortcut": {"key": "s", "modifiers": []}, "OSC": {"commands":[]}}

    # Miscellaneous
    LABEL = {"shortcut": {"key": "l", "modifiers": []}, "OSC": {"commands":[]}}
    PART = {"shortcut": {"key": "p", "modifiers": []}, "OSC": {"commands":[]}}
    INTENSITY_FILTER = {"shortcut": {"key": "i", "modifiers": [Key.ctrl]}, "OSC": {"commands":[]}}
    COLOR_FILTER = {"shortcut": {"key": "c", "modifiers": [Key.ctrl]}, "OSC": {"commands":[]}}
    EFFECT = {"shortcut": {"key": "e", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    SNAPSHOT = {"shortcut": {"key": "s", "modifiers": [Key.ctrl]}, "OSC": {"commands":[]}}
    TIME = {"shortcut": {"key": "i", "modifiers": []}, "OSC": {"commands":[]}}
    TIME_DISPLAY = {"shortcut": {"key": "i", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    RATE = {"shortcut": {"key": "r", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    OFFSET = {"shortcut": {"key": "o", "modifiers": [Key.ctrl]}, "OSC": {"commands":[]}}
    QUERY = {"shortcut": {"key": "q", "modifiers": [Key.ctrl]}, "OSC": {"commands":[]}}
    PARK = {"shortcut": {"key": "k", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    STOP_EFFECT = {"shortcut": {"key": "e", "modifiers": [Key.shift, Key.alt]}, "OSC": {"commands":[]}}
    MAGIC_SHEET = {"shortcut": {"key": "m", "modifiers": [Key.alt]}, "OSC": {"commands":[]}}
    MACRO_801 = {"shortcut": {"key": "1", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_802 = {"shortcut": {"key": "2", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_803 = {"shortcut": {"key": "3", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_804 = {"shortcut": {"key": "4", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_805 = {"shortcut": {"key": "5", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_806 = {"shortcut": {"key": "6", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_807 = {"shortcut": {"key": "7", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_808 = {"shortcut": {"key": "8", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_809 = {"shortcut": {"key": "9", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}
    MACRO_810 = {"shortcut": {"key": "0", "modifiers": [Key.ctrl, Key.alt]}, "OSC": {"commands":[]}}


words_to_commands = {
    "live": Command.LIVE,
    "blind": Command.BLIND,
    "staging": Command.STAGING,
    "zero": Command.ZERO, "one": Command.ONE,
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

    "follow": Command.FOLLOW,
    "hang": Command.HANG,

    "cue": Command.CUE,
    "at": Command.AT,
    "at at": Command.ATAT,
    "at level": Command.ATAT,
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
    "stop back": Command.STOP_BACK,
    "stop": Command.STOP_BACK,
    "back": Command.STOP_BACK,
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
