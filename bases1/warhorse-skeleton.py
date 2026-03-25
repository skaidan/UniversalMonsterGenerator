# bases1/warhorse-skeleton.py
"""
WarhorseSkeleton creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warhorse-skeleton
"""
from creature_base import GlobalCreatureBaseClass


class WarhorseSkeleton(GlobalCreatureBaseClass):
    """
    Large undead creature - WarhorseSkeleton
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 12, 'CON': 15, 'INT': 2, 'WIS': 8, 'CHAR': 5, 'armor_class': 13, 'alignment': 'lawful evil Armor Class  13 (barding scraps) Hit Points  22 (3d10 + 6) Speed  60 ft. STR 18 (+4) DEX 12 (+1) CON 15 (+2) INT 2 (-4) WIS 8 (-1) CHA 5 (-3) Damage Vulnerabilities  bludgeoning Damage Immunities  poison Condition Immunities  exhaustion', 'legendary': False, 'size': 'Large', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

