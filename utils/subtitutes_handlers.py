# All function involving concatenation of the commands from the DB.
# Everything should be replaced here so the command would smoothly run as a shell command


# Used when printing Data on screen. Change $VALUE when showing the user commands.
def substitute_placeholder(command: str, holder: str, key: str, ) -> str:
    return command.replace(holder, key)


# Ensure every Command List should have 3 indexes. Fill them with empty string
def split_min_3(input_str: str) -> list:
    parts = input_str.strip().split(maxsplit=2)  # Limit to 3 elements
    while len(parts) < 3:
        parts.append("")  # Pad with empty strings
    return parts


# Accepts a single string. Single string should be one command. Not chained
def normalize_command(command: str) -> list:
    from app_data.en.english_strings import session_configuration_commands as scc
    from app_data.en.english_strings import session_configuration_options as sco
    from app_data.en.english_strings import navigation_keywords as nav

    operator, key, value = split_min_3(command)
    normlized_command = [substitute_alias(operator, scc), substitute_alias(key, sco), value]
    # For Navigation related, the above code return "" as operator for any navigational commands.
    if normlized_command[0] == "":
        normlized_command[0] = substitute_alias(operator, nav)
    return normlized_command


# Dynamically load the dict and use it to normalize the input
def substitute_alias(input_word: str, key_pairs: dict) -> str:
    matched = ""
    for keyword, alias in sorted(key_pairs.items(), key=lambda item: -len(str(item[1]))):
        if input_word.lower() in alias:
            matched = keyword
            break
    return matched
