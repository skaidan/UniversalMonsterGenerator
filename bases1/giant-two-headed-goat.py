# bases1/giant-two-headed-goat.py
"""
GiantTwoHeadedGoat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-two-headed-goat
"""
from creature_base import GlobalCreatureBaseClass


class GiantTwoHeadedGoat(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantTwoHeadedGoat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 11, 'CON': 12, 'INT': 3, 'WIS': 12, 'CHAR': 6, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 (natural armor) Hit Points  19 (3d10 + 3) Speed  40 ft. STR 17 (+3) DEX 11 (+0) CON 12 (+1) INT 3 (-4) WIS 12 (+1) CHA 6 (-2) Senses  passive Perception 11 Languages  — Challenge  1/2 (100 XP) Charge . If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'multiattack', 'ram']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 5 (2d4) bludgeoning damage. If the target is a creature, it m"""
        return 'If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 5 (2d4) bludgeoning damage. If the target is a creature, it m'

    def multiattack_attack(self) -> str:
        """The two-headed goat makes two ram attacks. These attacks must be against different targets."""
        return 'The two-headed goat makes two ram attacks. These attacks must be against different targets.'

    def ram_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) bludgeoning damage.'

