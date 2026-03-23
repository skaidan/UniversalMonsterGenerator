# bases1/sea-hag.py
"""
SeaHag creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sea-hag
"""
from creature_base import GlobalCreatureBaseClass


class SeaHag(GlobalCreatureBaseClass):
    """
    SeaHag creature
    Size: Medium, Type: fey, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fey, chaotic evil",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The hag can breathe air and water.Horrific Appearance. Any humanoid that starts its turn within 30 f..."""
        return "The hag can breathe air and water.Horrific Appearance. Any humanoid that starts its turn within 30 feet of the hag and can see the hag's true form must make a DC 11 Wisdom saving throw. On a failed sa"
    def amphibious(self) -> str:
        """Amphibious: The hag can breathe air and water.Horrific Appearance. Any humanoid that starts its turn within 30 f..."""
        return "The hag can breathe air and water.Horrific Appearance. Any humanoid that starts its turn within 30 feet of the hag and can see the hag's true form must make a DC 11 Wisdom saving throw. On a failed sa"

