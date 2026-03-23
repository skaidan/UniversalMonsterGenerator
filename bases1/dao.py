# bases1/dao.py
"""
Dao creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dao
"""
from creature_base import GlobalCreatureBaseClass


class Dao(GlobalCreatureBaseClass):
    """
    Dao creature
    Size: Huge, Type: or smaller creature, it must succeed on a DC 18 Strength check or be knocked prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 187,
        "min_level": 12,
        "level": 12,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "or smaller creature, it must succeed on a DC 18 Strength check or be knocked prone.",
        "hit_points_up": [18, 18, 18],
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
        """Earth Glide: The dao can burrow through nonmagical, unworked earth and stone. While doing so, the dao doesn't dis..."""
        return "The dao can burrow through nonmagical, unworked earth and stone. While doing so, the dao doesn't disturb the material it moves through.Elemental Demise. If the dao dies, its body disintegrates into cr"
    def earth_glide(self) -> str:
        """Earth Glide: The dao can burrow through nonmagical, unworked earth and stone. While doing so, the dao doesn't dis..."""
        return "The dao can burrow through nonmagical, unworked earth and stone. While doing so, the dao doesn't disturb the material it moves through.Elemental Demise. If the dao dies, its body disintegrates into cr"

