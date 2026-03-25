# bases1/guard-drake.py
"""
GuardDrake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=guard-drake
"""
from creature_base import GlobalCreatureBaseClass


class GuardDrake(GlobalCreatureBaseClass):
    """
    Medium Dragon creature - GuardDrake
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 16, 'INT': 4, 'WIS': 10, 'CHAR': 7, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  52 (7d8 + 21) Speed  30 ft. STR 16 (+3) DEX 11 (+0) CON 16 (+3) INT 4 (-3) WIS 10 (+0) CHA 7 (-2) Skills  Perception +2 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'tail']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The guard drake makes one Bite attack and one Tail attack."""
        return 'The guard drake makes one Bite attack and one Tail attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.'

