import os
import requests
import dotenv
from pythonosc import udp_client
from commands import command_string_to_command

dotenv.load_dotenv()

client = udp_client.SimpleUDPClient(os.getenv("OSC_IP"), int(os.getenv("OSC_PORT")))
receiving_client = udp_client.SimpleUDPClient(os.getenv("OSC_IP"), int(os.getenv("OSC_LISTEN_PORT")))


def get_system_prompt():
    with open("system_prompt.txt", "r") as file:
        return file.read()

def convert_to_etc_eos_command(input_value, model_id):
    prompt = [
        {"role": "system", "content": get_system_prompt()},
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
        print(response)
        # execute_commands(response)
