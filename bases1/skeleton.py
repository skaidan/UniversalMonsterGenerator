# bases1/skeleton.py
"""
Skeleton creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=skeleton
"""
from creature_base import GlobalCreatureBaseClass


class Skeleton(GlobalCreatureBaseClass):
    """
    Medium undead creature - Skeleton
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 15, 'INT': 6, 'WIS': 8, 'CHAR': 5, 'armor_class': 13, 'alignment': 'lawful evil Armor Class  13 (armor scraps) Hit Points  13 (2d8 + 4) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 15 (+2) INT 6 (-2) WIS 8 (-1) CHA 5 (-3) Damage Vulnerabilities  bludgeoning Damage Immunities  poison Condition Immunities  exhaustion', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shortsword', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

