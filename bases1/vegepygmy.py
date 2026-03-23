# bases1/vegepygmy.py
"""
Vegepygmy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vegepygmy
"""
from creature_base import GlobalCreatureBaseClass


class Vegepygmy(GlobalCreatureBaseClass):
    """
    Vegepygmy creature
    Size: Small, Type: Plant, typically Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "Plant, typically Neutral",
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
        self.abilities.extend(['plant_camouflage'])

    def plant_camouflage(self) -> str:
        """Plant Camouflage: The vegepygmy has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuri..."""
        return "The vegepygmy has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The vegepygmy regains 3 hit points at the start of its turn. If it takes"

