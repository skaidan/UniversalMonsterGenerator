# bases1/earth-elemental.py
"""
EarthElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=earth-elemental
"""
from creature_base import GlobalCreatureBaseClass


class EarthElemental(GlobalCreatureBaseClass):
    """
    EarthElemental creature
    Size: Large, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 126,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "elemental, neutral",
        "hit_points_up": [12, 12, 12],
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
        self.abilities.extend(['earth_glide'])

    def earth_glide(self) -> str:
        """Earth Glide: The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental..."""
        return "The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through.Siege Monster. The elemental deals double damage to o"
    def earth_glide(self) -> str:
        """Earth Glide: The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental..."""
        return "The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through.Siege Monster. The elemental deals double damage to o"

