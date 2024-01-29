from .UserPost import UserPost

class User(UserPost):
    id: int

    class Config:
        from_attributes = True