# bases1/bestial-spirit.py
"""
BestialSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bestial-spirit
"""
from creature_base import GlobalCreatureBaseClass


class BestialSpirit(GlobalCreatureBaseClass):
    """
    BestialSpirit creature
    Size: Small, Type: beast, -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 20,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "beast, -",
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
        # Add creature-specific abilities
        self.abilities.extend(['flyby_air_only'])

    def flyby_air_only(self) -> str:
        """Flyby (Air Only): The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach.Pack Tactics (La..."""
        return "The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach.Pack Tactics (Land and Water Only). The beast has advantage on an attack roll against a creature if at least one of "

