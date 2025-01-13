import os
import requests
import dotenv
from utils import number_string_to_number, number_to_words
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from commands import words_to_commands, number_words, command_string_to_command

dotenv.load_dotenv()

client = udp_client.SimpleUDPClient(os.getenv("OSC_IP"), int(os.getenv("OSC_PORT")))
receiving_client = udp_client.SimpleUDPClient(os.getenv("OSC_IP"), int(os.getenv("OSC_LISTEN_PORT")))

def convert_to_etc_eos_command(input_value, model_id):
    prompt = [
        {"role": "system", "content": "Convert to ETC EOS command"},
        {"role": "user", "content": input_value}
    ]

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
            },
            json={
                "model": model_id,
                "messages": prompt
            }
        )
        return response.json()
    except Exception as e:
        print("Error sending message to OpenAI:", e)
        raise

def execute_commands(commands):
    """
    Should take in the output of command_string_to_commands and execute the commands
    """
    # split input into list (split by " ")
    command_list = commands.split(" ")
    for command in command_list:
        send(command_string_to_command(command))


def send(command_dict):
    for command in command_dict["commands"]:
        client.send_message(command, [])

if __name__ == "__main__":
    model_id = "ft:gpt-4o-mini-2024-07-18:personal::Ao7vsIaL"
    while True:
        input_value = input("Ask EOS...\n")
        response = convert_to_etc_eos_command(input_value, model_id).get("choices")[0].get("message").get("content")
        execute_commands(response)
