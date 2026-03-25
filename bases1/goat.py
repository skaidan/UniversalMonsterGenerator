# bases1/goat.py
"""
Goat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=goat
"""
from creature_base import GlobalCreatureBaseClass


class Goat(GlobalCreatureBaseClass):
    """
    Medium beast creature - Goat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 4, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 10, 'CON': 11, 'INT': 2, 'WIS': 10, 'CHAR': 5, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  4 (1d8) Speed  40 ft. STR 12 (+1) DEX 10 (+0) CON 11 (+0) INT 2 (-4) WIS 10 (+0) CHA 5 (-3) Senses  passive Perception 10 Languages  — Challenge  0 (10 XP) Charge . If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'ram']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 2 (1d4) bludgeoning damage. If the target is a creature, it m"""
        return 'If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 2 (1d4) bludgeoning damage. If the target is a creature, it m'

    def ram_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage.'

