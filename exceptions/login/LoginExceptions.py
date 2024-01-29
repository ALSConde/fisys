from .ILoginException import ILoginException


class InvalidCredentials(ILoginException):
    def __init__(self) -> None:
        super().__init__("Invalid credentials")
