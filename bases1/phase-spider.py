# bases1/phase-spider.py
"""
PhaseSpider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=phase-spider
"""
from creature_base import GlobalCreatureBaseClass


class PhaseSpider(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - PhaseSpider
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 15, 'CON': 12, 'INT': 6, 'WIS': 10, 'CHAR': 6, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  32 (5d10 + 5) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['ethereal_jaunt', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def ethereal_jaunt(self) -> str:
        """As a bonus action, the spider can magically shift from the Material Plane to the Ethereal Plane, or vice versa.Spider Climb. The spider can climb difficult surfaces, including upside down on ceilings,"""
        return 'As a bonus action, the spider can magically shift from the Material Plane to the Ethereal Plane, or vice versa.Spider Climb. The spider can climb difficult surfaces, including upside down on ceilings,'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 18 (4d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 18 (4d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.'

