from random import randint

from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int

    def calculate_something(self) -> int:
        return randint(1, self.age)
