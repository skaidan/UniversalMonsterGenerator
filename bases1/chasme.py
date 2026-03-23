# bases1/chasme.py
"""
Chasme creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chasme
"""
from creature_base import GlobalCreatureBaseClass


class Chasme(GlobalCreatureBaseClass):
    """
    Chasme creature
    Size: Large, Type: fiend (Demon), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 84,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend (Demon), chaotic evil",
        "hit_points_up": [8, 8, 8],
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
        self.abilities.extend(['drone'])

    def drone(self) -> str:
        """Drone: The chasme produces a horrid droning sound to which demons are immune. Any other creature that start..."""
        return "The chasme produces a horrid droning sound to which demons are immune. Any other creature that starts its turn with in 30 feet of the chasme must succeed on a DC 12 Constitution saving throw or fall u"
    def drone(self) -> str:
        """Drone: The chasme produces a horrid droning sound to which demons are immune. Any other creature that start..."""
        return "The chasme produces a horrid droning sound to which demons are immune. Any other creature that starts its turn with in 30 feet of the chasme must succeed on a DC 12 Constitution saving throw or fall u"

