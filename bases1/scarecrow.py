# bases1/scarecrow.py
"""
Scarecrow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scarecrow
"""
from creature_base import GlobalCreatureBaseClass


class Scarecrow(GlobalCreatureBaseClass):
    """
    Scarecrow creature
    Size: Medium, Type: construct, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 36,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "construct, chaotic evil",
        "hit_points_up": [3, 3, 3],
        "STR_up": [1, 0, 0],
        "DEX_up": [1, 0, 0],
        "CON_up": [0, 1, 0],
        "INT_up": [0, 1, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 1],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the scarecrow remains motionless, it is indistinguishable from an ordinary, inanimate scarecro..."""
        return "While the scarecrow remains motionless, it is indistinguishable from an ordinary, inanimate scarecrow.ActionsMultiattack. The scarecrow makes two claw attacks.Claw. Melee Weapon Attack: +3 to hit, rea"
    def false_appearance(self) -> str:
        """False Appearance: While the scarecrow remains motionless, it is indistinguishable from an ordinary, inanimate scarecro..."""
        return "While the scarecrow remains motionless, it is indistinguishable from an ordinary, inanimate scarecrow.ActionsMultiattack. The scarecrow makes two claw attacks.Claw. Melee Weapon Attack: +3 to hit, rea"

