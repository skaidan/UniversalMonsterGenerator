# bases1/giant-elk.py
"""
GiantElk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-elk
"""
from creature_base import GlobalCreatureBaseClass


class GiantElk(GlobalCreatureBaseClass):
    """
    Huge beast creature - GiantElk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 42, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 16, 'CON': 14, 'INT': 7, 'WIS': 14, 'CHAR': 10, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  42 (5d12 + 10) Speed  60 ft. STR 19 (+4) DEX 16 (+3) CON 14 (+2) INT 7 (-2) WIS 14 (+2) CHA 10 (+0) Skills  Perception +4 Senses  passive Perception 14 Languages  Giant Elk understands Common', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'ram', 'hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed o"""
        return 'If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed o'

    def ram_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one prone creature. Hit: 22 (4d8 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one prone creature. Hit: 22 (4d8 + 4) bludgeoning damage.'

