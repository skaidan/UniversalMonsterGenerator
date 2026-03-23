# bases2/base2_a.py
from creature_base import GlobalCreatureBaseClass


class Base2A(GlobalCreatureBaseClass):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("MagicResistance")

    def method2(self) -> None:
        print("Base2A.method2")
