# bases1/carrion-crawler.py
"""
CarrionCrawler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=carrion-crawler
"""
from creature_base import GlobalCreatureBaseClass


class CarrionCrawler(GlobalCreatureBaseClass):
    """
    CarrionCrawler creature
    Size: Large, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 51,
        "min_level": 3,
        "level": 3,
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
        self.abilities.extend(['keen_smell'])

    def keen_smell(self) -> str:
        """Keen Smell: The carrion crawler has advantage on Wisdom (Perception) checks that rely on smell.Spider Climb. The..."""
        return "The carrion crawler has advantage on Wisdom (Perception) checks that rely on smell.Spider Climb. The carrion crawler can climb difficult surfaces, including upside down on ceilings, without needing to"
    def keen_smell(self) -> str:
        """Keen Smell: The carrion crawler has advantage on Wisdom (Perception) checks that rely on smell.Spider Climb. The..."""
        return "The carrion crawler has advantage on Wisdom (Perception) checks that rely on smell.Spider Climb. The carrion crawler can climb difficult surfaces, including upside down on ceilings, without needing to"

