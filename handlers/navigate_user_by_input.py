from modules.local_classes import LocalHostConfigurations as LocalH
from modules.remote_classes import RemoteHostConfigurations as RemoteH
from utils.backend_operations import load_file_to_json, configure_host_object, is_integer
from utils.subtitutes_handlers import normalize_command
from handlers.additional_communication import take_input_from_user, load_show_menu, show_commands, actions_to_move_back
from app_data.en.english_strings import full_manual_string

# The main and first script that really interacts with a user
# Take input > determine what to print.
# user_input is already validated as an int. Take the int and match it to a valid option from the current path


# In case the user is moving within the files the stack will arrive here.
def handle_motion_within_db(user_input: str, lhost_configuration: LocalH, rhost_configuration: RemoteH) -> None:
    current_options = load_file_to_json(lhost_configuration.current_json_path)
    max_choice = len(current_options)
    # Validate the input is within the options
    if int(user_input) <= max_choice:
        # If data is a dictionary, it is a list of commands.
        if isinstance(current_options[user_input]["data"], dict):
            show_commands(current_options[user_input]["data"], lhost_configuration, rhost_configuration)
        # Incase the data is a string, it will be a path to a different file.
        elif isinstance(current_options[user_input]["data"], str):
            lhost_configuration.configure("json_path", current_options[user_input]["data"])
            load_show_menu(lhost_configuration.current_json_path)
        else:
            print("Corner-case #01223")
    else:
        load_show_menu(lhost_configuration.current_json_path)
        print(f"Invalid choice. The highest valid option is {max_choice}, but you entered {user_input}.")


# The operator received will direct to it's action
def handle_configuration(user_input: list, lhost_configuration: LocalH, rhost_configuration: RemoteH) -> None:
    operator, key, value = user_input
    if operator in {"get", "run"}:
        print("Wait for the next version please :)")
        return
    if operator == "unset":
        # Change value to it's default status. Default Value: $VALUE: string
        default_placeholder = f"${key.upper()}"
        configure_host_object(key, default_placeholder, lhost_configuration, rhost_configuration)
        return
    if operator == "set":
        configure_host_object(key, value, lhost_configuration, rhost_configuration)
        return


# Every command from the user will end up in this function.
def filter_options_by_users_input(user_income_command: str, lhost: LocalH, rhost: RemoteH) -> None:
    if is_integer(user_income_command):
        handle_motion_within_db(user_income_command, lhost, rhost)
        return
    else:
        try:
            lowered_command = normalize_command(user_income_command)
            command_map = {
                "quit": lambda: exit("Sad to see you go. Bye bye :)"),
                "menu": lambda: load_show_menu(lhost.current_json_path),
                "help": lambda: print(full_manual_string),
                "back": lambda: actions_to_move_back(lhost),
            }

            if lowered_command[0] in command_map:
                command_map[lowered_command[0]]()

        # Turn the command into a string that fit the standard
            handle_configuration(lowered_command, lhost, rhost)
        except ValueError:
            print(f"I can't understand this: {user_income_command}.")
        except KeyError:
            print(f"KeyError encountered with input: {user_income_command}.")
        except Exception:
            print(f"Corner-case #00013")


# Script access point!
def take_user_input_round(lhost_object: LocalH, rhost_object: RemoteH) -> None:
    user_income_command = take_input_from_user()
    if user_income_command == "":
        print("Empty message received. Now what?")
        return

    # Incase the input contain ";" this function will treat it as command within a list. Avoid trailing ; and /
    commands: list[str] = [command.strip() for command in user_income_command.strip(";").strip("/").split(";") if command.strip()]

    # TODO: handle cases such ma;ma;ma;
    amount = len(commands)
    if amount == 1:
        filter_options_by_users_input(commands[0], lhost_object, rhost_object)
    elif amount > 1:
        for command in commands:
            filter_options_by_users_input(command, lhost_object, rhost_object)
    else:
        print("Corner-Case #00003")
