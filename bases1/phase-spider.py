# bases1/phase-spider.py
"""
PhaseSpider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=phase-spider
"""
from creature_base import GlobalCreatureBaseClass


class PhaseSpider(GlobalCreatureBaseClass):
    """
    PhaseSpider creature
    Size: Large, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 32,
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
        "type": "monstrosity, unaligned",
        "hit_points_up": [3, 3, 3],
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
        self.abilities.extend(['ethereal_jaunt'])

    def ethereal_jaunt(self) -> str:
        """Ethereal Jaunt: As a bonus action, the spider can magically shift from the Material Plane to the Ethereal Plane, or ..."""
        return "As a bonus action, the spider can magically shift from the Material Plane to the Ethereal Plane, or vice versa.Spider Climb. The spider can climb difficult surfaces, including upside down on ceilings,"
    def ethereal_jaunt(self) -> str:
        """Ethereal Jaunt: As a bonus action, the spider can magically shift from the Material Plane to the Ethereal Plane, or ..."""
        return "As a bonus action, the spider can magically shift from the Material Plane to the Ethereal Plane, or vice versa.Spider Climb. The spider can climb difficult surfaces, including upside down on ceilings,"

