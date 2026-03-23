# bases1/base1_b.py
from creature_base import GlobalCreatureBaseClass


class Base1B(GlobalCreatureBaseClass):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("Invisibility")

    def method1b(self) -> None:
        print("Base1B method1b")
