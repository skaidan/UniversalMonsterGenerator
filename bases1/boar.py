# bases1/boar.py
"""
Boar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=boar
"""
from creature_base import GlobalCreatureBaseClass


class Boar(GlobalCreatureBaseClass):
    """
    Medium beast creature - Boar
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 11, 'CON': 12, 'INT': 2, 'WIS': 9, 'CHAR': 5, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 (natural armor) Hit Points  11 (2d8 + 2) Speed  40 ft. STR 13 (+1) DEX 11 (+0) CON 12 (+1) INT 2 (-4) WIS 9 (-1) CHA 5 (-3) Senses  passive Perception 9 Languages  — Challenge  1/4 (50 XP) Charge . If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'tusk']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 3 (1d6) slashing damage. If the target is a creature, it mus"""
        return 'If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 3 (1d6) slashing damage. If the target is a creature, it mus'

    def tusk_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.'

