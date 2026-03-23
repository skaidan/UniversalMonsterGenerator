# bases1/banderhobb.py
"""
Banderhobb creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=banderhobb
"""
from creature_base import GlobalCreatureBaseClass


class Banderhobb(GlobalCreatureBaseClass):
    """
    Banderhobb creature
    Size: Medium, Type: or smaller creature grappled by the banderhobb.
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
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature grappled by the banderhobb.",
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
        self.abilities.extend(['resonant_connection'])

    def resonant_connection(self) -> str:
        """Resonant Connection: If the banderhobb has even a tiny piece of a creature or an object in its possession, such as a lock..."""
        return "If the banderhobb has even a tiny piece of a creature or an object in its possession, such as a lock of hair or a splinter of wood, it knows the most direct route to that creature or object if it is w"

