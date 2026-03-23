# bases1/piercer.py
"""
Piercer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=piercer
"""
from creature_base import GlobalCreatureBaseClass


class Piercer(GlobalCreatureBaseClass):
    """
    Piercer creature
    Size: Medium, Type: monstrosity, unaligned
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
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "monstrosity, unaligned",
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the piercer remains motionless on the ceiling, it is indistinguishable from a normal stalactit..."""
        return "While the piercer remains motionless on the ceiling, it is indistinguishable from a normal stalactite.Spider Climb. The piercer can climb difficult surfaces, including upside down on ceilings, without"
    def false_appearance(self) -> str:
        """False Appearance: While the piercer remains motionless on the ceiling, it is indistinguishable from a normal stalactit..."""
        return "While the piercer remains motionless on the ceiling, it is indistinguishable from a normal stalactite.Spider Climb. The piercer can climb difficult surfaces, including upside down on ceilings, without"

