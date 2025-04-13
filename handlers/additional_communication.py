from utils.subtitutes_handlers import substitute_placeholder
from handlers.input_validation_handlers import sanitize_strings
from modules.remote_classes import RemoteHostConfigurations as RemoteH
from modules.local_classes import LocalHostConfigurations as LocalH
from utils.backend_operations import load_file_to_json


def localhost_substitutions(lhost_configuration: LocalH):
    return [
        lambda d: substitute_placeholder(d, "$LHOST", lhost_configuration.lhost),
        lambda d: substitute_placeholder(d, "$LPORT", lhost_configuration.lport),
        lambda d: substitute_placeholder(d, "$PROXY", lhost_configuration.proxy),
        lambda d: substitute_placeholder(d, "$AWSPROFILE", lhost_configuration.nic),
        lambda d: substitute_placeholder(d, "$NIC", lhost_configuration.nic)
    ]


def remotehost_substitutions(rhost_configuration: RemoteH):
    return [
        lambda d: substitute_placeholder(d, "$RHOST", rhost_configuration.rhost),
        lambda d: substitute_placeholder(d, "$RPORT", rhost_configuration.rport),
        lambda d: substitute_placeholder(d, "$DOMAIN", rhost_configuration.domain),
        lambda d: substitute_placeholder(d, "$PATH", rhost_configuration.path),
        lambda d: substitute_placeholder(d, "$USERNAME", rhost_configuration.username),
        lambda d: substitute_placeholder(d, "$PASSWORD", rhost_configuration.password),
        lambda d: substitute_placeholder(d, "$USERNAMES", rhost_configuration.usernames),
        lambda d: substitute_placeholder(d, "$PASSWORDS", rhost_configuration.passwords),
        lambda d: substitute_placeholder(d, "$WORDLIST", rhost_configuration.wordlist)
    ]


def show_commands(protocol_commands: dict, local_host: LocalH, remote_host: RemoteH) -> None:
    substitutions = localhost_substitutions(local_host) + remotehost_substitutions(remote_host)

    for key, value in protocol_commands.items():
        for function in substitutions:
            value = function(value)
        print(f"# {key}:\n{value}\n")


# The menu which display
def load_show_menu(current_path: str) -> None:
    options = load_file_to_json(current_path)
    for key, data in options.items():
        print(f"{key}:{data['name']}")


# Function to basic validate the entire input. Also, chained commands will user this
def take_input_from_user():
    user_input = input("$: ")
    safer_string = user_input.strip().lower()
    if sanitize_strings(safer_string):
        return user_input


# Used after returning the last JSONed options
def actions_to_move_back(lhost: LocalH) -> None:
    if lhost.current_json_path != "./app_data/commands/main_menu.json":
        lhost.configure("json_path", lhost.last_json_path)
        load_show_menu(lhost.current_json_path)
    else:
        print("This is the root. Can't go back from here! MuhahHAhahA")
