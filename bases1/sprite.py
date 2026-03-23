# bases1/sprite.py
"""
Sprite creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sprite
"""
from creature_base import GlobalCreatureBaseClass


class Sprite(GlobalCreatureBaseClass):
    """
    Sprite creature
    Size: Tiny, Type: fey, neutral good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 2,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "fey, neutral good",
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
        self.abilities.extend(['longsword'])

    def longsword(self) -> str:
        """Longsword: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 slashing damage.Shortbow. Ranged Wea..."""
        return "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 slashing damage.Shortbow. Ranged Weapon Attack: +6 to hit, range 40/160 ft., one target. Hit: 1 piercing damage, and the target must suc"
    def longsword(self) -> str:
        """Longsword: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 slashing damage.Shortbow. Ranged Wea..."""
        return "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 slashing damage.Shortbow. Ranged Weapon Attack: +6 to hit, range 40/160 ft., one target. Hit: 1 piercing damage, and the target must suc"

