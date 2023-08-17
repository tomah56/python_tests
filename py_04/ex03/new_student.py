import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    """Your docstring for Class"""
    name: str
    surname: str
    active: bool = True
    login: str = None
    id: str = generate_id

    def __post_init__(self):
        self.login = self.create_login()

    def create_login(self):
        return self.name[0] + self.surname
    # def __init__(self, name, surname):
    #     """Your docstring for Constructor"""
    #     self.name = name
    #     self.nicknaem = surname
    #     self.active = True
    #     self.login = name[0] + surname
    #     self.id = generate_id
    #     self.print()
