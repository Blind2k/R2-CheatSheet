#!/usr/bin/env python3

from modules.local_classes import LocalHostConfigurations as LocalH
from modules.remote_classes import RemoteHostConfigurations as RemoteH
from handlers.navigate_user_by_input import take_user_input_round
from handlers.additional_communication import load_show_menu
import os

# Get the directory where this file is located
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
# Move to the project root
os.chdir(SCRIPT_DIR)


# The main function that should last forever. This is where the interactive part repeats itself
def main() -> None:
    # The following should be further developed in the future
    local_host_object = LocalH()
    remote_host_object = RemoteH()

    print("Welcome to the R2-Cheat Sheet")
    load_show_menu(local_host_object.current_json_path)
    while True:
        take_user_input_round(local_host_object, remote_host_object)


# This is the first line that should be executed.
if __name__ == "__main__":
    main()
