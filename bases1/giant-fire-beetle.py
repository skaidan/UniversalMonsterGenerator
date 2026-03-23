# bases1/giant-fire-beetle.py
"""
GiantFireBeetle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-fire-beetle
"""
from creature_base import GlobalCreatureBaseClass


class GiantFireBeetle(GlobalCreatureBaseClass):
    """
    GiantFireBeetle creature
    Size: Small, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 4,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
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
        self.abilities.extend(['illumination'])

    def illumination(self) -> str:
        """Illumination: The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet.ActionsBit..."""
        return "The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet.ActionsBite. Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) slashing damage.A giant"
    def illumination(self) -> str:
        """Illumination: The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet.ActionsBit..."""
        return "The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet.ActionsBite. Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) slashing damage.A giant"

