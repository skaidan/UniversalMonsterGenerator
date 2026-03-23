# bases1/female-steeder.py
"""
FemaleSteeder creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=female-steeder
"""
from creature_base import GlobalCreatureBaseClass


class FemaleSteeder(GlobalCreatureBaseClass):
    """
    FemaleSteeder creature
    Size: Medium, Type: or smaller creature.
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
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature.",
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
        # Add creature-specific abilities
        self.abilities.extend(['extraordinary_leap'])

    def extraordinary_leap(self) -> str:
        """Extraordinary Leap: The distance of the steeder's long jumps is tripled; every foot of its walking speed that it spends ..."""
        return "The distance of the steeder's long jumps is tripled; every foot of its walking speed that it spends on the jump allows it to move 3 feet.Spider Climb. The steeder can climb difficult surfaces, includi"

