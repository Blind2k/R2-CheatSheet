from modules.class_validation_helpers import BaseValidationHelpers


# Object to gather what's relevant to the remote computer and the current attack
class RemoteHostConfigurations(BaseValidationHelpers):
    """
    Class below regarding remote configurations. AKA your current target.
    Set and get configuration.
    """
    def __init__(self):
        super().__init__()
        self._rhost: str = "$RHOST"
        self._rport: str = "$RPORT"
        self._domain: str = "$DOMAIN"
        self._path: str = "$PATH"
        self._username: str = "$USERNAME"
        self._password: str = "$PASSWORD"
        self._usernames: str = "$USERNAMES"
        self._passwords: str = "$PASSWORDS"
        self._wordlist: str = "$WORDLIST"

# Method to set what's ever needed after initialization
    def configure(self, key: str, value: str):
        match key:
            case "rhost":
                self.rhost = value
            case "rport":
                self.rport = value
            case "domain":
                self.domain = value
            case "path":
                self.path = value
            case "username":
                self.username = value
            case "password":
                self.password = value
            case "usernames":
                self.usernames = value
            case "passwords":
                self.passwords = value
            case "wordlist":
                self.wordlist = value
            case _:
                raise ValueError(f"Unknown configuration key: {key}")

    """ Getters & Setters configuration """
    # RHOST
    @property
    def rhost(self) -> str:
        return self._rhost

    @rhost.setter
    def rhost(self, value: str):
        self._rhost = self._validate_address(value, "$RHOST")

    # RPORT
    @property
    def rport(self) -> str:
        return self._rport

    @rport.setter
    def rport(self, value: str):
        self._rport = self._validate_port(value, "$RPORT")

    # DOMAIN/AD
    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, value: str):
        self._domain = self._validate_address(value, "$DOMAIN")

    # PATH
    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str):
        self._path = self._path = self._validate_string(value)

    # USERNAME
    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = self._username = self._validate_string(value)

    # PASSWORD
    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = self._password = self._validate_string(value)

    # FILE: USERNAME
    @property
    def usernames(self) -> str:
        return self._usernames

    @usernames.setter
    def usernames(self, value: str) -> None:
        self._usernames = self._usernames = self._validate_file(value, "$USERNAMES")

    # FILE: PASSWORD
    @property
    def passwords(self) -> str:
        return self._passwords

    @passwords.setter
    def passwords(self, value: str) -> None:
        self._passwords = self._validate_file(value, "$PASSWORDS")

    # FILE: WORDLIST
    @property
    def wordlist(self) -> str:
        return self._wordlist

    @wordlist.setter
    def wordlist(self, value: str) -> None:
        self._wordlist = self._validate_file(value, "$WORDLIST")

