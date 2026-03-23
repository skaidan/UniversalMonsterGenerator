# bases1/flameskull.py
"""
Flameskull creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flameskull
"""
from creature_base import GlobalCreatureBaseClass


class Flameskull(GlobalCreatureBaseClass):
    """
    Flameskull creature
    Size: Tiny, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 40,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "undead, neutral evil",
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
        self.abilities.extend(['illumination'])

    def illumination(self) -> str:
        """Illumination: The flameskull sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and d..."""
        return "The flameskull sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and dim light for an additional 15 feet. It can switch between the options as an action.Magic Resistance."
    def illumination(self) -> str:
        """Illumination: The flameskull sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and d..."""
        return "The flameskull sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and dim light for an additional 15 feet. It can switch between the options as an action.Magic Resistance."

