# bases1/minor-earth-elemental.py
"""
MinorEarthElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minor-earth-elemental
"""
from creature_base import GlobalCreatureBaseClass


class MinorEarthElemental(GlobalCreatureBaseClass):
    """
    MinorEarthElemental creature
    Size: Small, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 60,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "elemental, neutral",
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
        # Add creature-specific abilities
        self.abilities.extend(['downhill_roller'])

    def downhill_roller(self) -> str:
        """Downhill Roller: The elemental's walking speed increases to 30 while moving downhill. If it moves at least 15 feet st..."""
        return "The elemental's walking speed increases to 30 while moving downhill. If it moves at least 15 feet straight towards a target and then hits it with a slam attack on the same turn, the target takes an ex"

