# bases1/nightmare.py
"""
Nightmare creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nightmare
"""
from creature_base import GlobalCreatureBaseClass


class Nightmare(GlobalCreatureBaseClass):
    """
    Nightmare creature
    Size: Large, Type: fiend, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 68,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend, neutral evil",
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
        self.abilities.extend(['confer_fire_resistance'])

    def confer_fire_resistance(self) -> str:
        """Confer Fire Resistance: The nightmare can grant resistance to fire damage to anyone riding it.Illumination. The nightmare sh..."""
        return "The nightmare can grant resistance to fire damage to anyone riding it.Illumination. The nightmare sheds bright light in a 10-foot radius and dim light for an additional 10 feet.ActionsHooves. Melee We"
    def confer_fire_resistance(self) -> str:
        """Confer Fire Resistance: The nightmare can grant resistance to fire damage to anyone riding it.Illumination. The nightmare sh..."""
        return "The nightmare can grant resistance to fire damage to anyone riding it.Illumination. The nightmare sheds bright light in a 10-foot radius and dim light for an additional 10 feet.ActionsHooves. Melee We"

