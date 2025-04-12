# All function involving concatenation of the commands from the DB.
# Everything should be replaced here so the command would smoothly run as a shell command


def subtitute_placeholder(command: str, holder: str, key: str,) -> str:
    return command.replace(holder, key)


def substitute_key_alias(input_word: str) -> str:
    from app_data.en.english_strings import session_configuration_options as sco

    key_pairs = {
        "rhost": sco["rhost"],
        "rport": sco["rport"],
        "domain": sco["domain"],
        "path": sco["path"],
        "username": sco["username"],
        "password": sco["password"],
        "usernames": sco["usernames"],
        "passwords": sco["passwords"],
        "wordlist": sco["wordlist"],
        "lhost": sco["lhost"],
        "lport": sco["lport"],
        "nic": sco["nic"]
    }
    # Begin search from the longer word. Had problem with password/passwords
    matched = None
    for keyword, alias in sorted(key_pairs.items(), key=lambda x: -len(str(x[1]))):
        if input_word.lower() in str(alias).lower():
            matched = keyword
            break
    return matched


def substitute_operator_alias(input_word: str) -> str:
    from app_data.en.english_strings import session_configuration_commands as scc
    key_pairs = {
        "run": scc["run"],
        "set": scc["set"],
        "unset": scc["unset"],
        "get": scc["get"]
    }
    for keyword, alias in key_pairs.items():
        if input_word.lower() in alias:
            return keyword


def normalize_command(command: list) -> list:
    length = len(command)
    if length == 2:
        return [command[0], command[1]]
    operator, key, value = command
    return [substitute_operator_alias(operator), substitute_key_alias(key), value]

