# bases1/scorpion.py
"""
Scorpion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scorpion
"""
from creature_base import GlobalCreatureBaseClass


class Scorpion(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Scorpion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 11, 'CON': 8, 'INT': 1, 'WIS': 8, 'CHAR': 2, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 (natural armor) Hit Points  1 (1d4 - 1) Speed  10 ft. STR 2 (-4) DEX 11 (+0) CON 8 (-1) INT 1 (-5) WIS 8 (-1) CHA 2 (-4) Senses  blindsight 10 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['sting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sting_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must make a DC 9 Constitution saving throw, taking 4 (1d8) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must make a DC 9 Constitution saving throw, taking 4 (1d8) poison damage on a failed save, or half as much damage on a successful one.'

