# bases1/gnoll-fang-of-yeenoghu.py
"""
GnollFangOfYeenoghu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll-fang-of-yeenoghu
"""
from creature_base import GlobalCreatureBaseClass


class GnollFangOfYeenoghu(GlobalCreatureBaseClass):
    """
    Medium fiend (Gnoll) creature - GnollFangOfYeenoghu
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 65, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 15, 'CON': 15, 'INT': 10, 'WIS': 11, 'CHAR': 13, 'armor_class': 14, 'alignment': 'chaotic evil Armor Class  14 (hide armor) Hit Points  65 (10d8 + 20) Speed  30 ft. STR 17 (+3) DEX 15 (+2) CON 15 (+2) INT 10 (+0) WIS 11 (+0) CHA 13 (+1) Saving Throws  Con +4', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Gnoll)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['rampage', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def rampage(self) -> str:
        """When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."""
        return 'When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack.'

    def multiattack_attack(self) -> str:
        """The gnoll makes three attacks: one with its bite and two with its claws."""
        return 'The gnoll makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 6 (1d6 + 3) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or take 7 (2d6) poison damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 6 (1d6 + 3) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or take 7 (2d6) poison damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d 8 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d 8 + 3) slashing damage.'

