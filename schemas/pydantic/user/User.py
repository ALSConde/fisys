from pydantic import ConfigDict
from .UserPost import UserPost


class User(UserPost):
    id: int

    model_config = ConfigDict(from_attributes=True)