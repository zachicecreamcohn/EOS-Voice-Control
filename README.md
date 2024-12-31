# EOS Voice Control

Using Vosk, Kaldi, and pynput, control EOS with your voice. This program uses OSC over UDP to send commands to your console.

This project is a work in progress and is not yet ready for production use but may still be helpful. Though the remote apps are great, there are times when I've been the only person in the room, on a ladder, and needed to make changes. This solves that problem (along with some wireless headphones).


## Installation

```
pip install -r requirements.txt
```

Create an `.env` file with the following contents:

```
OSC_IP=192.169.1.7 # your console's IP
OSC_PORT=9000 # your console's OSC UDP RX port (configure in System > Show Control > OSC)
```

## Usage

```
python main.py
```



# TODO
- [ ] Implement context-specific grammar.
- [x] Add mute/unmute shortcut/hotkey
- [ ] Fine tune to improve accuracy with my voice [using Vosk's model training](https://alphacephei.com/vosk/adaptation#:~:text=Adapting%20the%20acoustic%20model%20with%20finetuning)
