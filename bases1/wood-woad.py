# bases1/wood-woad.py
"""
WoodWoad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wood-woad
"""
from creature_base import GlobalCreatureBaseClass


class WoodWoad(GlobalCreatureBaseClass):
    """
    WoodWoad creature
    Size: Large, Type: or bigger.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 75,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or bigger.",
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
        # Add creature-specific abilities
        self.abilities.extend(['plant_camouflage'])

    def plant_camouflage(self) -> str:
        """Plant Camouflage: The wood woad has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuri..."""
        return "The wood woad has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The wood woad regains 10 hit points at the start of its turn if it is in"

