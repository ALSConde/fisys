
from typing import Generic, TypeVar


M = TypeVar('M')

class AbstractValidator(Generic[M]):
    def validate(self, model: M) -> None:
        raise NotImplementedError