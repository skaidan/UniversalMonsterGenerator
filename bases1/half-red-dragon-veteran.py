# bases1/half-red-dragon-veteran.py
"""
HalfRedDragonVeteran creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=half-red-dragon-veteran
"""
from creature_base import GlobalCreatureBaseClass


class HalfRedDragonVeteran(GlobalCreatureBaseClass):
    """
    HalfRedDragonVeteran creature
    Size: Medium, Type: humanoid (Human), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 65,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Human), any alignment",
        "hit_points_up": [6, 6, 6],
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
        """Multiattack: The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword..."""
        return "The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword attack.Longsword. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashin"
    def multiattack(self) -> str:
        """Multiattack: The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword..."""
        return "The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword attack.Longsword. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashin"

