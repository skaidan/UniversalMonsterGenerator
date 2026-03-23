# bases1/giant-hyena.py
"""
GiantHyena creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-hyena
"""
from creature_base import GlobalCreatureBaseClass


class GiantHyena(GlobalCreatureBaseClass):
    """
    GiantHyena creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['rampage'])

    def rampage(self) -> str:
        """Rampage: When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can tak..."""
        return "When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can take a bonus action to move up to half its speed and make a bite attack.ActionsBite. Melee Weapon Attac"
    def rampage(self) -> str:
        """Rampage: When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can tak..."""
        return "When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can take a bonus action to move up to half its speed and make a bite attack.ActionsBite. Melee Weapon Attac"

