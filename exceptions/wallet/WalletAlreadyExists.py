from exceptions.APIError import APIError


class WalletAlreadyExists(APIError):
    def __init__(self, message: str = "Wallet already exists"):
        super().__init__(409, message)
