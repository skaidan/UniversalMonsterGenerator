# bases2/base2_b.py
from creature_base import GlobalCreatureBaseClass


class Base2B(GlobalCreatureBaseClass):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("MagicResistance")

    def method2b(self) -> None:
        print("Base2B.method2b")
