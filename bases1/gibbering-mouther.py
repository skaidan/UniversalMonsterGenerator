# bases1/gibbering-mouther.py
"""
GibberingMouther creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gibbering-mouther
"""
from creature_base import GlobalCreatureBaseClass


class GibberingMouther(GlobalCreatureBaseClass):
    """
    GibberingMouther creature
    Size: Medium, Type: or smaller, it must succeed on a DC 10 Strength saving throw or be knocked prone. If the target is killed by this damage, it is absorbed into the mouther.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 67,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 9,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, it must succeed on a DC 10 Strength saving throw or be knocked prone. If the target is killed by this damage, it is absorbed into the mouther.",
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
        self.abilities.extend(['aberrant_ground'])

    def aberrant_ground(self) -> str:
        """Aberrant Ground: The ground in a 10-foot radius around the mouther is doughlike difficult terrain. Each creature that..."""
        return "The ground in a 10-foot radius around the mouther is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have itsSpeed reduced"
    def aberrant_ground(self) -> str:
        """Aberrant Ground: The ground in a 10-foot radius around the mouther is doughlike difficult terrain. Each creature that..."""
        return "The ground in a 10-foot radius around the mouther is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have itsSpeed reduced"

