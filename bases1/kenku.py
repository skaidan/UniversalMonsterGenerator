# bases1/kenku.py
"""
Kenku creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kenku
"""
from creature_base import GlobalCreatureBaseClass


class Kenku(GlobalCreatureBaseClass):
    """
    Kenku creature
    Size: Medium, Type: humanoid (Kenku), chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
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
        "type": "humanoid (Kenku), chaotic neutral",
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
        self.abilities.extend(['ambusher'])

    def ambusher(self) -> str:
        """Ambusher: In the first round of a combat, the kenku has advantage on attack rolls against any creature it surp..."""
        return "In the first round of a combat, the kenku has advantage on attack rolls against any creature it surprised.Mimicry. The kenku can mimic any sounds it has heard, including voices. A creature that hears "
    def ambusher(self) -> str:
        """Ambusher: In the first round of a combat, the kenku has advantage on attack rolls against any creature it surp..."""
        return "In the first round of a combat, the kenku has advantage on attack rolls against any creature it surprised.Mimicry. The kenku can mimic any sounds it has heard, including voices. A creature that hears "

