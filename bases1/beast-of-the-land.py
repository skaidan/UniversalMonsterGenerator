# bases1/beast-of-the-land.py
"""
BeastOfTheLand creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=beast-of-the-land
"""
from creature_base import GlobalCreatureBaseClass


class BeastOfTheLand(GlobalCreatureBaseClass):
    """
    BeastOfTheLand creature
    Size: Medium, Type: beast, -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 5,
        "min_level": 1,
        "level": 1,
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
        "type": "beast, -",
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
        # Add creature-specific abilities
        self.abilities.extend(['charge'])

    def charge(self) -> str:
        """Charge: If the beast moves at least 20 feet straight toward a target and then hits it with a maul attack on ..."""
        return "If the beast moves at least 20 feet straight toward a target and then hits it with a maul attack on the same turn, the target takes an extra 1d6 slashing damage. If the target is a creature, it must s"

