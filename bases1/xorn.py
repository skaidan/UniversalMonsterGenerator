# bases1/xorn.py
"""
Xorn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=xorn
"""
from creature_base import GlobalCreatureBaseClass


class Xorn(GlobalCreatureBaseClass):
    """
    Xorn creature
    Size: Medium, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 73,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "elemental, neutral",
        "hit_points_up": [7, 7, 7],
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
        """Earth Glide: The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't d..."""
        return "The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't disturb the material it moves through.Stone Camouflage. The xorn has advantage on Dexterity (Stealth)"
    def earth_glide(self) -> str:
        """Earth Glide: The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't d..."""
        return "The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't disturb the material it moves through.Stone Camouflage. The xorn has advantage on Dexterity (Stealth)"

