from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
from pynput.keyboard import Controller
from commands import words_to_commands, number_words
from utils import number_string_to_number, number_to_words

MODEL_PATH = "vosk-model-small-en-us-0.15"
model = Model(MODEL_PATH)

grammar = json.dumps(number_words + list(words_to_commands.keys()))
recognizer = KaldiRecognizer(model, 16000, grammar)

keyboard = Controller()

def send(command_dict):
    for mod in command_dict["modifiers"]:
        keyboard.press(mod)
    if command_dict["key"]:
        keyboard.press(command_dict["key"])
        keyboard.release(command_dict["key"])
    for mod in reversed(command_dict["modifiers"]):
        keyboard.release(mod)

def get_commands_from_phrase(phrase):
    if phrase in words_to_commands:
        return [words_to_commands[phrase].value]
    try:
        number = number_string_to_number(phrase)
        result = []
        for digit in str(number):
            word_for_digit = number_to_words(int(digit))
            if word_for_digit in words_to_commands:
                result.append(words_to_commands[word_for_digit].value)
            else:
                result.append(digit)
        return result
    except ValueError:
        return None

def execute_command(full_command):
    tokens = full_command.split()
    i = 0

    while i < len(tokens):
        largest_match = None
        largest_match_cmds = None

        for j in range(i + 1, len(tokens) + 1):
            phrase = " ".join(tokens[i:j])
            cmds = get_commands_from_phrase(phrase)
            if cmds is not None:
                largest_match = j
                largest_match_cmds = cmds

        if largest_match is not None:
            for cmd_or_char in largest_match_cmds:
                if isinstance(cmd_or_char, dict):
                    send(cmd_or_char)
                else:
                    keyboard.type(cmd_or_char)
            i = largest_match
        else:
            print(f"Unrecognized: {tokens[i]}")
            i += 1

def audio_callback(indata, frames, time, status):
    audio_data = indata.tobytes()
    if recognizer.AcceptWaveform(audio_data):
        result = json.loads(recognizer.Result())
        if "text" in result:
            command = result["text"]
            print(f"Recognized: {command}")
            execute_command(command)

def main():
    print("Listening for commands...")
    with sd.InputStream(samplerate=16000, channels=1, dtype="int16", callback=audio_callback):
        sd.sleep(-1)

if __name__ == "__main__":
    main()
