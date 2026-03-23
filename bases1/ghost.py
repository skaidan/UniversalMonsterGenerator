# bases1/ghost.py
"""
Ghost creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ghost
"""
from creature_base import GlobalCreatureBaseClass


class Ghost(GlobalCreatureBaseClass):
    """
    Ghost creature
    Size: Medium, Type: undead, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, any alignment",
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
        self.abilities.extend(['ethereal_sight'])

    def ethereal_sight(self) -> str:
        """Ethereal Sight: The ghost can see 60 feet into the Ethereal Plane when it is on the Material Plane, and vice versa.I..."""
        return "The ghost can see 60 feet into the Ethereal Plane when it is on the Material Plane, and vice versa.Incorporeal Movement. The ghost can move through other creatures and objects as if they were difficul"
    def ethereal_sight(self) -> str:
        """Ethereal Sight: The ghost can see 60 feet into the Ethereal Plane when it is on the Material Plane, and vice versa.I..."""
        return "The ghost can see 60 feet into the Ethereal Plane when it is on the Material Plane, and vice versa.Incorporeal Movement. The ghost can move through other creatures and objects as if they were difficul"

