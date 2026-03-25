# bases1/carrion-crawler.py
"""
CarrionCrawler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=carrion-crawler
"""
from creature_base import GlobalCreatureBaseClass


class CarrionCrawler(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - CarrionCrawler
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 51, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 13, 'CON': 16, 'INT': 1, 'WIS': 12, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  51 (6d10 + 18) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'multiattack', 'tentacles', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The carrion crawler has advantage on Wisdom (Perception) checks that rely on smell.Spider Climb. The carrion crawler can climb difficult surfaces, including upside down on ceilings, without needing to"""
        return 'The carrion crawler has advantage on Wisdom (Perception) checks that rely on smell.Spider Climb. The carrion crawler can climb difficult surfaces, including upside down on ceilings, without needing to'

    def multiattack_attack(self) -> str:
        """The carrion crawler makes two attacks: one with its tentacles and one with its bite."""
        return 'The carrion crawler makes two attacks: one with its tentacles and one with its bite.'

    def tentacles_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one creature. Hit: 4 (1d4 + 2) poison damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 minute. Until this poison ends, the target is paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the poison on itself on a success."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one creature. Hit: 4 (1d4 + 2) poison damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 minute. Until this poison ends, the target is paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the poison on itself on a success.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage.'

