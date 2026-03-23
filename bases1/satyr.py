# bases1/satyr.py
"""
Satyr creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=satyr
"""
from creature_base import GlobalCreatureBaseClass


class Satyr(GlobalCreatureBaseClass):
    """
    Satyr creature
    Size: Medium, Type: fey, chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 31,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fey, chaotic neutral",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The satyr has advantage on saving throws against spells and other magical effects.ActionsRam. Melee ..."""
        return "The satyr has advantage on saving throws against spells and other magical effects.ActionsRam. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) bludgeoning damage.Shortsword. M"
    def magic_resistance(self) -> str:
        """Magic Resistance: The satyr has advantage on saving throws against spells and other magical effects.ActionsRam. Melee ..."""
        return "The satyr has advantage on saving throws against spells and other magical effects.ActionsRam. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) bludgeoning damage.Shortsword. M"

