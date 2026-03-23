# bases1/basilisk.py
"""
Basilisk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=basilisk
"""
from creature_base import GlobalCreatureBaseClass


class Basilisk(GlobalCreatureBaseClass):
    """
    Basilisk creature
    Size: Medium, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "monstrosity, unaligned",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['petrifying_gaze'])

    def petrifying_gaze(self) -> str:
        """Petrifying Gaze: If a creature starts its turn within 30 feet of the basilisk and the two of them can see each other,..."""
        return "If a creature starts its turn within 30 feet of the basilisk and the two of them can see each other, the basilisk can force the creature to make a DC 12 Constitution saving throw if the basilisk isn't"
    def petrifying_gaze(self) -> str:
        """Petrifying Gaze: If a creature starts its turn within 30 feet of the basilisk and the two of them can see each other,..."""
        return "If a creature starts its turn within 30 feet of the basilisk and the two of them can see each other, the basilisk can force the creature to make a DC 12 Constitution saving throw if the basilisk isn't"

