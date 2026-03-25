# bases1/gnoll-pack-lord.py
"""
GnollPackLord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll-pack-lord
"""
from creature_base import GlobalCreatureBaseClass


class GnollPackLord(GlobalCreatureBaseClass):
    """
    Medium humanoid (Gnoll) creature - GnollPackLord
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 49, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 13, 'INT': 8, 'WIS': 11, 'CHAR': 9, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Gnoll)', 'challenge': '0', 'saving_throws': None, 'skills': None, 'damage_resistances': None, 'damage_immunities': None, 'condition_immunities': None, 'senses': 'darkvision 60 ft., passive Perception 10', 'languages': None, 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['rampage', 'multiattack', 'bite', 'glaive', 'longbow', 'incite_rampage_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def rampage(self) -> str:
        """When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."""
        return 'When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack.'

    def multiattack_attack(self) -> str:
        """The gnoll makes two attacks, either with its glaive or its longbow, and uses its Incite Rampage if it can."""
        return 'The gnoll makes two attacks, either with its glaive or its longbow, and uses its Incite Rampage if it can.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) piercing damage.'

    def glaive_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 8 (1d10 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 8 (1d10 + 3) slashing damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

    def incite_rampage_(recharge_5-6)_attack(self) -> str:
        """One creature the gnoll can see within 30 feet of it can use its reaction to make a melee attack if it can hear the gnoll and has the Rampage trait."""
        return 'One creature the gnoll can see within 30 feet of it can use its reaction to make a melee attack if it can hear the gnoll and has the Rampage trait.'

