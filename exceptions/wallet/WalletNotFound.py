from exceptions.APIError import APIError


class WalletNotFound(APIError):
    def __init__(self, message: str = "Wallet not found"):
        super().__init__(404, message)
