# bases2/base2_a.py
from creature_base import GlobalCreatureBaseClass


class Base2D(GlobalCreatureBaseClass):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("MagicResistance")

    def method2(self) -> None:
        print("Base2D.method2")
