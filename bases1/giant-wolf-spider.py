# bases1/giant-wolf-spider.py
"""
GiantWolfSpider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-wolf-spider
"""
from creature_base import GlobalCreatureBaseClass


class GiantWolfSpider(GlobalCreatureBaseClass):
    """
    Medium beast creature - GiantWolfSpider
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 16, 'CON': 13, 'INT': 3, 'WIS': 12, 'CHAR': 4, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  11 (2d8 + 2) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['spider_climb', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def spider_climb(self) -> str:
        """The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.Web Sense. While in contact with a web, the spider knows the exact location of any """
        return 'The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.Web Sense. While in contact with a web, the spider knows the exact location of any '

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 7 (2d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 7 (2d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.'

