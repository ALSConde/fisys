from exceptions.APIError import APIError


class UserNotFound(APIError):
    def __init__(self, message: str = "User not found"):
        super().__init__(404, message)
