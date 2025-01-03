from enum import Enum
from utils import number_to_words

class Command(Enum):
    """
    Commands to shortcut mappings for keyboard.send
    """

    DO_NOTHING = {"commands":[]}

    # Numbers and Symbols
    ZERO = {"commands":["/eos/key/0"]}
    ONE = {"commands":["/eos/key/1"]}
    TWO = {"commands":["/eos/key/2"]}
    THREE = {"commands":["/eos/key/3"]}
    FOUR = {"commands":["/eos/key/4"]}
    FIVE = {"commands":["/eos/key/5"]}
    SIX = {"commands":["/eos/key/6"]}
    SEVEN = {"commands":["/eos/key/7"]}
    EIGHT = {"commands":["/eos/key/8"]}
    NINE = {"commands":["/eos/key/9"]}
    DECIMAL = {"commands":["/eos/key/."]}
    MINUS = {"commands":["/eos/key/-"]}
    PLUS = {"commands":["/eos/key/+"]}
    PLUS_PERCENT = {"commands":["/eos/key/+%"]}
    MINUS_PERCENT = {"commands":["/eos/key/-$"]}
    DIVIDE = {"commands":["/eos/key//"]}

    # Console Modes
    LIVE = {"commands":["/eos/key/live"]}
    BLIND = {"commands":["/eos/key/blind"]}
    STAGING = {"commands":[]} # TODO: determine the command for this

    # Common Commands
    CUE = {"commands":["/eos/key/cue"]}
    AT = {"commands":["/eos/key/@"]}
    ATAT = {"commands":["/eos/key/@", "/eos/key/@"]}
    OUT = {"commands":["/eos/key/out"]}
    THRU = {"commands":["/eos/key/thru"]}
    UPDATE = {"commands":["/eos/key/update"]}
    GROUP = {"commands":["/eos/key/group"]}
    ENTER = {"commands":["/eos/key/enter"]}
    GOTOCUE = {"commands":["/eos/key/go_to_cue"]}
    FULL = {"commands":["/eos/key/full"]}
    CLEAR = {"commands":["/eos/key/clear_cmd"]}
    SHIFT_CLEAR = {"commands":["/eos/key/clear_cmdline"]}
    DELETE = {"commands":["/eos/key/delete"]}
    GO = {"commands":["/eos/key/go_0"]}
    STOP_BACK = {"commands":["/eos/key/stop"]}
    HOME = {"commands":["/eos/key/home"]}
    MARK = {"commands":["/eos/key/mark"]}
    RECALLFROM = {"commands":["/eos/key/recall_from"]}
    SHIFT = {"commands":["/eos/key/shift"]} # TODO: Make sure this works properly since it's something that needs to be "held down" and not typed into the command ine
    SNEAK = {"commands":["/eos/key/sneak"]}
    PATCH = {"commands":["/eos/key/patch"]}
    RECORD = {"commands":["/eos/key/record"]}
    RECORD_ONLY = {"commands":["/eos/key/record_only"]}
    UNDO = {"commands":["/eos/key/undo"]}
    FOLLOW = {"commands":["/eos/key/follow"]}
    HANG = {"commands":["/eos/key/hang"]}
    SOLO = {"commands":["/eos/key/solo"]}
    REM_DIM = {"commands":["/eos/key/rem_dim"]}



    # Navigation and Camera
    NEXT = {"commands":["/eos/key/next"]}
    LAST = {"commands":["/eos/key/last"]}

    # System Controls
    ESCAPE = {"commands":["/eos/key/escape"]}
    TAB = {"commands":["/eos/key/tab"]}
    EXPAND = {"commands":["/eos/key/expand"]}
    FLEXI_CHANNEL = {"commands":["/eos/key/flexi_all"]}
    DISPLAYS = {"commands":["/eos/key/displays"]}

    # Softkeys and Submaster
    SOFTKEY_1 = {"commands":["/eos/key/softkey_1"]}
    SOFTKEY_2 = {"commands":["/eos/key/softkey_2"]}
    SOFTKEY_3 = {"commands":["/eos/key/softkey_3"]}
    SOFTKEY_4 = {"commands":["/eos/key/softkey_4"]}
    SOFTKEY_5 = {"commands":["/eos/key/softkey_5"]}
    SOFTKEY_6 = {"commands":["/eos/key/softkey_6"]}
    SOFTKEY_7 = {"commands":["/eos/key/softkey_7"]}
    SOFTKEY_8 = {"commands":["/eos/key/softkey_8"]}

    SUBMASTER = {"commands":["/eos/key/sub"]}

    # Miscellaneous
    LABEL = {"commands":["/eos/key/label"]}
    PART = {"commands":["/eos/key/part"]}
    INTENSITY = {"commands":["/eos/key/intensity"]}
    COLOR = {"commands":["/eos/key/color"]}
    EFFECT = {"commands":["/eos/key/effect"]}
    SNAPSHOT = {"commands":["/eos/key/snapshot"]}
    TIME = {"commands":["/eos/key/time"]}
    RATE = {"commands":["/eos/key/rate"]}
    OFFSET = {"commands":["/eos/key/offset"]}
    QUERY = {"commands":["/eos/key/query"]}
    PARK = {"commands":["/eos/key/park"]}
    STOP_EFFECT = {"commands":["/eos/key/stop_effect"]}
    MAGIC_SHEET = {"commands":["/eos/key/magic_sheet"]}
    MOVE_TO = {"commands":["/eos/key/move_to"]}
    COPY_TO = {"commands":["/eos/key/copy_to"]}
    MACRO = {"commands":["/eos/key/macro"]}

    FOCUS_PALETTE = {"commands":["/eos/key/focus_palette"]}
    BEAM_PALETTE = {"commands":["/eos/key/beam_palette"]}
    COLOR_PALETTE = {"commands":["/eos/key/color_palette"]}

    # TODO: Add more (obscure or less used by me) commands from [these docs](https://community.troikatronix.com/assets/uploads/files/FileUpload/f8/c8d85d-eos-osc-keys.pdf?v=lmfj8m1vhl4)
    # - [ ] Rem Dim
    # - [ ] Delay

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
    "and": Command.PLUS,
    "slash": Command.DIVIDE,

    "follow": Command.FOLLOW,
    "hang": Command.HANG,
    "solo": Command.SOLO,

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
    "fool": Command.FULL,
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
    "escape": Command.ESCAPE,
    "tab": Command.TAB,
    "expand": Command.EXPAND,
    "flexi channel": Command.FLEXI_CHANNEL,
    "displays": Command.DISPLAYS,
    "softkey one": Command.SOFTKEY_1,
    "softkey two": Command.SOFTKEY_2,
    "softkey three": Command.SOFTKEY_3,
    "softkey four": Command.SOFTKEY_4,
    "softkey five": Command.SOFTKEY_5,
    "softkey six": Command.SOFTKEY_6,
    "softkey seven": Command.SOFTKEY_7,
    "softkey eight": Command.SOFTKEY_8,
    "submaster": Command.SUBMASTER,
    "label": Command.LABEL,
    "part": Command.PART,
    "intensity": Command.INTENSITY,
    "color": Command.COLOR,
    "effect": Command.EFFECT,
    "snapshot": Command.SNAPSHOT,
    "time": Command.TIME,
    "rate": Command.RATE,
    "offset": Command.OFFSET,
    "query": Command.QUERY,
    "park": Command.PARK,
    "stop effect": Command.STOP_EFFECT,
    "magic sheet": Command.MAGIC_SHEET,
    "move to": Command.MOVE_TO,
    "copy to": Command.COPY_TO,
    "macro": Command.MACRO,
    "focus palette": Command.FOCUS_PALETTE,
    "beam palette": Command.BEAM_PALETTE,
    "color palette": Command.COLOR_PALETTE,
    "rem dim": Command.REM_DIM,

    # Common words that shouldn't do anything
    # These are often used colloquially but don't have a direct command mapping
    "channel": Command.DO_NOTHING,
    "channels": Command.DO_NOTHING,
    "light": Command.DO_NOTHING,
    "lights": Command.DO_NOTHING,


}


number_words = [number_to_words(i) for i in range(1001)]
