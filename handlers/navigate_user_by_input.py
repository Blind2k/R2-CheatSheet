from modules.local_classes import LocalHostConfigurations as LocalH
from modules.remote_classes import RemoteHostConfigurations as RemoteH
from utils.backend_operations import load_file_to_json, configure_host_object
from utils.subtitutes_handlers import normalize_command
from handlers.additional_communication import take_input_from_user, load_show_menu, show_commands, actions_to_move_back
from app_data.en.english_strings import (full_manual_string, print_menu_keywords, exit_script_keywords, ask_help_keywords,
                                         back_one_keywords)


# The main and first script that really interacts with a user
# Take input > determine what to print.
# user_input is already validated as an int. Take the int and match it to a valid option from the current path
def handle_motion_within_db(user_input: str, lhost_configuration: LocalH, rhost_configuration: RemoteH) -> None:
    current_options = load_file_to_json(lhost_configuration.current_json_path)
    max_choice = len(current_options)
    if int(user_input) <= max_choice:
        if isinstance(current_options[user_input]["data"], dict):
            show_commands(current_options[user_input]["data"], lhost_configuration, rhost_configuration)
        elif isinstance(current_options[user_input]["data"], str):
            lhost_configuration.configure("json_path", current_options[user_input]["data"])
            load_show_menu(lhost_configuration.current_json_path)
        else:
            print("Corner-Ccase #01223")
    else:
        load_show_menu(lhost_configuration.current_json_path)
        print(f"Invalid choice. The highest valid option is {max_choice}, but you entered {user_input}.")


def handle_configuration(user_input: list, lhost_configuration: LocalH, rhost_configuration: RemoteH) -> None:
    operator = user_input[0]
    key = str(user_input[1])
    if operator == "run":
        print("Wait for next version")
        return
    if operator == "unset":
        default_placeholder = f"${key.upper()}"
        configure_host_object(key, default_placeholder, lhost_configuration, rhost_configuration)
        return
    operator, key, value = user_input
    if operator == "set":
        configure_host_object(key, value, lhost_configuration, rhost_configuration)
        return
    print("Something with the command is wrong")


def filter_options_by_users_input(user_income_command: str, lhost: LocalH, rhost: RemoteH) -> None:
    if user_income_command == "":
        return

    try:
        if user_income_command.isdigit():
            handle_motion_within_db(user_income_command, lhost, rhost)
            return

        special_commands = {
            tuple(exit_script_keywords): lambda: exit("Sad to see you go. Bye bye :)"),
            tuple(print_menu_keywords): lambda: load_show_menu(lhost.current_json_path),
            tuple(ask_help_keywords): lambda: print(full_manual_string),
            tuple(back_one_keywords): lambda: actions_to_move_back(lhost),
        }

        for keywords, action in special_commands.items():
            if user_income_command in keywords:
                action()
                return

        split_command = normalize_command(user_income_command.split())
        handle_configuration(split_command, lhost, rhost)
    except ValueError as error:
        print(f"ValueError encountered with input: {user_income_command}.")
    except KeyError as error:
        print(f"KeyError encountered with input: {user_income_command}.")
    except Exception as error:
        print(f"Corner-case #00013")


# set rhost 8.8.8.8; set rport 8080
# Script access point!
def take_user_input_round(lhost_object: LocalH, rhost_object: RemoteH) -> None:
    user_income_command = take_input_from_user()

    # Incase the input contain ";" this function will treat it as few commands
    # TODO: handle cases such ma;ma;ma;
    commands = [command.strip() for command in user_income_command.strip(";").strip("/").split(";") if command.strip()]

    amount = len(commands)
    if amount == 1:
        filter_options_by_users_input(commands[0], lhost_object, rhost_object)
    elif amount > 1:
        for command in commands:
            filter_options_by_users_input(command, lhost_object, rhost_object)
    else:
        print("Corner-Case #00003")

