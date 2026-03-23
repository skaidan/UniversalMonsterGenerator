# bases1/roper.py
"""
Roper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=roper
"""
from creature_base import GlobalCreatureBaseClass


class Roper(GlobalCreatureBaseClass):
    """
    Roper creature
    Size: Large, Type: monstrosity, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 93,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, neutral evil",
        "hit_points_up": [9, 9, 9],
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the roper remains motionless, it is indistinguishable from a normal cave formation, such as a ..."""
        return "While the roper remains motionless, it is indistinguishable from a normal cave formation, such as a stalagmite.Grasping Tendrils. The roper can have up to six tendrils at a time. Each tendril can be a"
    def false_appearance(self) -> str:
        """False Appearance: While the roper remains motionless, it is indistinguishable from a normal cave formation, such as a ..."""
        return "While the roper remains motionless, it is indistinguishable from a normal cave formation, such as a stalagmite.Grasping Tendrils. The roper can have up to six tendrils at a time. Each tendril can be a"

