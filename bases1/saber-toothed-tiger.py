# bases1/saber-toothed-tiger.py
"""
SaberToothedTiger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=saber-toothed-tiger
"""
from creature_base import GlobalCreatureBaseClass


class SaberToothedTiger(GlobalCreatureBaseClass):
    """
    Large beast creature - SaberToothedTiger
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 15, 'INT': 3, 'WIS': 12, 'CHAR': 8, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  52 (7d10 + 14) Speed  40 ft. STR 18 (+4) DEX 14 (+2) CON 15 (+2) INT 3 (-4) WIS 12 (+1) CHA 8 (-1) Skills  Perception +3', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The tiger has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the tiger moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, th"""
        return 'The tiger has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the tiger moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, th'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (1d10 + 5) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (1d10 + 5) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage.'

