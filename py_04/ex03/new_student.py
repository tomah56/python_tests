import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function ot generate id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Your docstring for Class"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default_factory=lambda: generate_id(), init=False)

    def __post_init__(self):
        """Post init generate login"""
        self.login = self.create_login()

    def create_login(self):
        """class method to generate the login"""
        return self.name[0] + self.surname
