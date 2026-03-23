# bases1/base1_a.py
from creature_base import GlobalCreatureBaseClass


class Base1A(GlobalCreatureBaseClass):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("ThiefTraining")

    def method1(self) -> None:
        print("Base1A.method1")
