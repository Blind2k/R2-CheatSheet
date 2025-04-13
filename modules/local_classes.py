from modules.class_validation_helpers import BaseValidationHelpers
from os import getcwd


class LocalHostConfigurations(BaseValidationHelpers):
    """
    Class below regarding local configurations.
    Set and get local host configuration options. Such as the owner (YOU!) IP, port, wordlists, etc.
    """
    def __init__(self):
        super().__init__()
        self._lhost: str = "$LHOST"
        self._lport: str = "$LPORT"
        self._nic: str = "$NIC"

        self._current_json_path: str = "./app_data/commands/main_menu.json"
        self._last_json_path: str = ""
        self._current_pwd: str = self.save_current_pwd()

        # TODO: Future development
        self._proxy: str = ""
        self._aws_profile: str = "$AWSPROFILE"

    def configure(self, key: str, value: str):
        match key:
            case "json_path":
                self._last_json_path = self._current_json_path
                self._current_json_path = value
            case "lhost":
                self.lhost = value
            case "lport":
                self.lport = value
            case "proxy":
                self.proxy = value
            case "aws_profile":
                self.aws_profile = value
            case "nic":
                self.nic = value
            case _:
                raise KeyError(f"Unknown configuration key: {key}")

    @staticmethod
    def save_current_pwd() -> str:
        return getcwd()

    # LHOST
    @property
    def lhost(self) -> str:
        return self._lhost

    @lhost.setter
    def lhost(self, value: str) -> None:
        self._lhost = self._validate_address(value, "$LHOST")

    # LPORT
    @property
    def lport(self) -> str:
        return self._lport

    @lport.setter
    def lport(self, value: str) -> None:
        self._lport = self._validate_port(value, "$LPORT")

    @property
    def current_json_path(self) -> str:
        return self._current_json_path

    @current_json_path.setter
    def current_json_path(self, value: str) -> None:
        self._current_json_path = self._validate_file(value, "./app_data/commands/main_menu.json")

    @property
    def last_json_path(self) -> str:
        return self._last_json_path

    # PROXY
    @property
    def proxy(self) -> str:
        return self._proxy

    @proxy.setter
    def proxy(self, value: str) -> None:
        self._proxy = self._validate_string(value)

    # AWS PROFILE
    @property
    def aws_profile(self) -> str:
        return self._aws_profile

    @aws_profile.setter
    def aws_profile(self, value: str) -> None:
        self._aws_profile = self._validate_string(value)

    @property
    def nic(self) -> str:
        return self._nic

    @nic.setter
    def nic(self, value: str) -> None:
        self._nic = self._validate_string(value)
