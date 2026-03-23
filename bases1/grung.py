# bases1/grung.py
"""
Grung creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grung
"""
from creature_base import GlobalCreatureBaseClass


class Grung(GlobalCreatureBaseClass):
    """
    Grung creature
    Size: Small, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
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
        "size": "Small",
        "type": "Humanoid, any alignment",
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwis..."""
        return "The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw "

