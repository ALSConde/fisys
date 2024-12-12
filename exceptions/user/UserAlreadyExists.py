from exceptions.APIError import APIError


class UserAlreadyExists(APIError):
    def __init__(self, message: str = "User already exists"):
        super().__init__(409, message)
