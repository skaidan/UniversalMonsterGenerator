# bases1/gray-ooze.py
"""
GrayOoze creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gray-ooze
"""
from creature_base import GlobalCreatureBaseClass


class GrayOoze(GlobalCreatureBaseClass):
    """
    GrayOoze creature
    Size: Medium, Type: ooze, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 8,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "ooze, unaligned",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['amorphous'])

    def amorphous(self) -> str:
        """Amorphous: The ooze can move through a space as narrow as 1 inch wide without squeezing.Corrode Metal. Any nonm..."""
        return "The ooze can move through a space as narrow as 1 inch wide without squeezing.Corrode Metal. Any nonmagical weapon made of metal that hits the ooze corrodes. After dealing damage, the weapon takes a pe"
    def amorphous(self) -> str:
        """Amorphous: The ooze can move through a space as narrow as 1 inch wide without squeezing.Corrode Metal. Any nonm..."""
        return "The ooze can move through a space as narrow as 1 inch wide without squeezing.Corrode Metal. Any nonmagical weapon made of metal that hits the ooze corrodes. After dealing damage, the weapon takes a pe"

