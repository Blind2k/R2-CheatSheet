# When defining a path, this function will ensure the file exists and contain data. Regardless if the data is valid.
# Functions here shouldn't have imports. Classes are an exclusion

def file_exists_and_not_empty(path: str) -> bool:
    from os.path import isfile, getsize
    return isfile(path) and getsize(path) > 0


# Load and iterate to create a JSON.
def load_file_to_json(file_path: str) -> dict:
    import json
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return {}


# Determine which Object (local/remote) contain the right attribute, so it could be changed
def configure_host_object(key: str, value: str, lhost_configuration: object, rhost_configuration: object) -> None:
    if hasattr(rhost_configuration, key):
        rhost_configuration.configure(key, value)
        print(f"{key}={value}")
    elif hasattr(lhost_configuration, key):
        lhost_configuration.configure(key, value)
        print(f"{key}={value}")
    else:
        print(f"Unknown configuration key: {key}")
