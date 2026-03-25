# bases1/rhinoceros.py
"""
Rhinoceros creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rhinoceros
"""
from creature_base import GlobalCreatureBaseClass


class Rhinoceros(GlobalCreatureBaseClass):
    """
    Large beast creature - Rhinoceros
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 8, 'CON': 15, 'INT': 2, 'WIS': 12, 'CHAR': 6, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 (natural armor) Hit Points  45 (6d10 + 12) Speed  40 ft. STR 21 (+5) DEX 8 (-1) CON 15 (+2) INT 2 (-4) WIS 12 (+1) CHA 6 (-2) Senses  passive Perception 11 Languages  — Challenge  2 (450 XP) Charge . If the rhinoceros moves at least 20 feet straight toward a target and then hits it with a gore attack on the same turn', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'gore']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the rhinoceros moves at least 20 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) bludgeoning damage. If the target is a creatur"""
        return 'If the rhinoceros moves at least 20 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) bludgeoning damage. If the target is a creatur'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage.'

