# bases1/catoblepas.py
"""
Catoblepas creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=catoblepas
"""
from creature_base import GlobalCreatureBaseClass


class Catoblepas(GlobalCreatureBaseClass):
    """
    Catoblepas creature
    Size: Large, Type: Monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 84,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Monstrosity, unaligned",
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
        # Add creature-specific abilities
        self.abilities.extend(['stench'])

    def stench(self) -> str:
        """Stench: Any creature other than a catoblepas that starts its turn within 10 feet of the catoblepas must succ..."""
        return "Any creature other than a catoblepas that starts its turn within 10 feet of the catoblepas must succeed on a DC 16 Constitution saving throw or be poisoned until the start of the creature's next turn."

