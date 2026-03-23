# bases1/half-ogre.py
"""
HalfOgre creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=half-ogre
"""
from creature_base import GlobalCreatureBaseClass


class HalfOgre(GlobalCreatureBaseClass):
    """
    HalfOgre creature
    Size: Large, Type: giant, any chaotic alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 30,
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
        "size": "Large",
        "type": "giant, any chaotic alignment",
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
        self.abilities.extend(['battleaxe'])

    def battleaxe(self) -> str:
        """Battleaxe: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2..."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2d10 + 3) slashing damage if used with two hands.Javelin. Melee or Ranged Weapon Attack: +5 to hit, r"
    def battleaxe(self) -> str:
        """Battleaxe: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2..."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2d10 + 3) slashing damage if used with two hands.Javelin. Melee or Ranged Weapon Attack: +5 to hit, r"

