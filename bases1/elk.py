# bases1/elk.py
"""
Elk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elk
"""
from creature_base import GlobalCreatureBaseClass


class Elk(GlobalCreatureBaseClass):
    """
    Large beast creature - Elk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 10, 'CON': 12, 'INT': 2, 'WIS': 10, 'CHAR': 6, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  13 (2d10 + 2) Speed  50 ft. STR 16 (+3) DEX 10 (+0) CON 12 (+1) INT 2 (-4) WIS 10 (+0) CHA 6 (-2) Senses  passive Perception 10 Languages  — Challenge  1/4 (50 XP) Charge . If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'ram', 'hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed o"""
        return 'If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed o'

    def ram_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one prone creature. Hit: 8 (2d4 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one prone creature. Hit: 8 (2d4 + 3) bludgeoning damage.'

