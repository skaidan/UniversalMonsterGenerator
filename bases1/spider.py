# bases1/spider.py
"""
Spider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spider
"""
from creature_base import GlobalCreatureBaseClass


class Spider(GlobalCreatureBaseClass):
    """
    Spider creature
    Size: Tiny, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 1,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "beast, unaligned",
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
        self.abilities.extend(['spider_climb'])

    def spider_climb(self) -> str:
        """Spider Climb: The spider can climb difficult surfaces, including upside down on ceilings, without needing to make ..."""
        return "The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.Web Sense. While in contact with a web, the spider knows the exact location of any "
    def spider_climb(self) -> str:
        """Spider Climb: The spider can climb difficult surfaces, including upside down on ceilings, without needing to make ..."""
        return "The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.Web Sense. While in contact with a web, the spider knows the exact location of any "

