# EOS Voice Control

Using Vosk, Kaldi, and pynput, control EOS with your voice. In practice, this can be used with your laptop either as a client or primary console with Nomand/a Gadget.

This project is a work in progress and is not yet ready for production use but may still be helpful. Though the remote apps are great, there are times when I've been the only person in the room, on a ladder, and needed to make changes. This solves that problem (along with some wireless headphones).

[Watch the demo](https://drive.google.com/file/d/11Fjp7LpDc_I5GnJm3mEfFMHJmwgPT4FA/view?usp=sharing)


## Installation

```
pip install -r requirements.txt
```

## Usage

```
python main.py
```

Note: you will need to have the EOS window in focus for the script to work.



# TODO
- [ ] Implement context-specific grammar.
- [x] Add mute/unmute shortcut/hotkey
- [ ] Fine tune to improve accuracy with my voice [using Vosk's model training](https://alphacephei.com/vosk/adaptation#:~:text=Adapting%20the%20acoustic%20model%20with%20finetuning)
