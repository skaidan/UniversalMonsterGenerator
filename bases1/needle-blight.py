# bases1/needle-blight.py
"""
NeedleBlight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=needle-blight
"""
from creature_base import GlobalCreatureBaseClass


class NeedleBlight(GlobalCreatureBaseClass):
    """
    NeedleBlight creature
    Size: Medium, Type: plant, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
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
        "type": "plant, neutral evil",
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
        self.abilities.extend(['claws'])

    def claws(self) -> str:
        """Claws: Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.Needles. R..."""
        return "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.Needles. Ranged Weapon Attack: +3 to hit, range 30/60 ft., one target. Hit: 8 (2d6 + 1) piercing damage.Monste"
    def claws(self) -> str:
        """Claws: Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.Needles. R..."""
        return "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.Needles. Ranged Weapon Attack: +3 to hit, range 30/60 ft., one target. Hit: 8 (2d6 + 1) piercing damage.Monste"

