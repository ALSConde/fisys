class APIError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return self.message

    def to_response(self):
        return {"message": self.message, "status_code": self.status_code}
