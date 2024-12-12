from exceptions.APIError import APIError


class InvalidCredentials(APIError):
    def __init__(self) -> None:
        super().__init__(401, "Invalid credentials")
