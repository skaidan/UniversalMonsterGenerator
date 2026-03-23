# bases1/magma-mephit.py
"""
MagmaMephit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=magma-mephit
"""
from creature_base import GlobalCreatureBaseClass


class MagmaMephit(GlobalCreatureBaseClass):
    """
    MagmaMephit creature
    Size: Small, Type: elemental, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "elemental, neutral evil",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['death_burst'])

    def death_burst(self) -> str:
        """Death Burst: When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a ..."""
        return "When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on"
    def death_burst(self) -> str:
        """Death Burst: When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a ..."""
        return "When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on"

