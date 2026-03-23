# bases1/ape.py
"""
Ape creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ape
"""
from creature_base import GlobalCreatureBaseClass


class Ape(GlobalCreatureBaseClass):
    """
    Ape creature
    Size: Medium, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 19,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "beast, unaligned",
        "hit_points_up": [1, 1, 1],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The ape makes two fist attacks.Fist. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6..."""
        return "The ape makes two fist attacks.Fist. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.Rock. Ranged Weapon Attack: +5 to hit, range 25/50 ft., one target. Hi"
    def multiattack(self) -> str:
        """Multiattack: The ape makes two fist attacks.Fist. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6..."""
        return "The ape makes two fist attacks.Fist. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.Rock. Ranged Weapon Attack: +5 to hit, range 25/50 ft., one target. Hi"

