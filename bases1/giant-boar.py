# bases1/giant-boar.py
"""
GiantBoar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-boar
"""
from creature_base import GlobalCreatureBaseClass


class GiantBoar(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantBoar
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 42, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 16, 'INT': 2, 'WIS': 7, 'CHAR': 5, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  42 (5d10 + 15) Speed  40 ft. STR 17 (+3) DEX 10 (+0) CON 16 (+3) INT 2 (-4) WIS 7 (-2) CHA 5 (-3) Senses  passive Perception 8 Languages  — Challenge  2 (450 XP) Charge . If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'tusk']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 7 (2d6) slashing damage. If the target is a creature, it mus"""
        return 'If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 7 (2d6) slashing damage. If the target is a creature, it mus'

    def tusk_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage.'

