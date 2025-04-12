from utils.backend_operations import file_exists_and_not_empty
from handlers.input_validation_handlers import validate_ip_or_domain


class BaseValidationHelpers:
    """
        This class inherits the LHOST and RHOST to validate values inside the Classes.
        1) String is a string?
        2) File exists and not empty?
        3) Is a valid port?
    """
    @staticmethod
    def _validate_string(value: str) -> str:
        if isinstance(value, str):
            return value
        raise ValueError(f"Invalid Type")

    @staticmethod
    def _validate_port(value: str, safeword: str) -> str:
        if (value.isdigit() and 1 <= int(value) <= 65535) or value == safeword:
            return str(value)
        raise ValueError(f"Invalid port number: {value}")

    @staticmethod
    def _validate_file(value: str, default_value: str) -> str:
        """ Helper function to check if the file exists and is not empty. """
        if isinstance(value, str):
            if file_exists_and_not_empty(value) or value == default_value:
                return value
            else:
                raise ValueError(f"The file {value} either doesn't exist or is empty.")
        else:
            raise ValueError(f"{value} must be a string.")

    @staticmethod
    def _validate_address(value: str, default_value: str) -> str:
        """ Helper function to validate IP or Domain. """
        if isinstance(value, str) and (validate_ip_or_domain(value) or value == default_value):
            return value
        else:
            raise ValueError(f"{value} must be a string.")
