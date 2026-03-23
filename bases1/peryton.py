# bases1/peryton.py
"""
Peryton creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=peryton
"""
from creature_base import GlobalCreatureBaseClass


class Peryton(GlobalCreatureBaseClass):
    """
    Peryton creature
    Size: Medium, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "monstrosity, chaotic evil",
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
        self.abilities.extend(['dive_attack'])

    def dive_attack(self) -> str:
        """Dive Attack: If the peryton is flying and dives at least 30 feet straight toward a target and then hits it with a..."""
        return "If the peryton is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 9 (2d8) damage to the target.Flyby. The peryton does"
    def dive_attack(self) -> str:
        """Dive Attack: If the peryton is flying and dives at least 30 feet straight toward a target and then hits it with a..."""
        return "If the peryton is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 9 (2d8) damage to the target.Flyby. The peryton does"

