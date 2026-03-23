# bases3/base3_a.py
from creature_base import GlobalCreatureBaseClass


class Base3B(GlobalCreatureBaseClass):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("Regeneration")

    def method3(self) -> None:
        print("Base3B.method3")
