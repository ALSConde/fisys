class APIError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __str__(self):
        return self.message

    def to_response(self):
        return {"message": self.message, "code": self.code}
