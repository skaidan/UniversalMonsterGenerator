# bases1/deer.py
"""
Deer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deer
"""
from creature_base import GlobalCreatureBaseClass


class Deer(GlobalCreatureBaseClass):
    """
    Medium beast creature - Deer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 4, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 11, 'INT': 2, 'WIS': 14, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  4 (1d8) Speed  50 ft. STR 11 (+0) DEX 16 (+3) CON 11 (+0) INT 2 (-4) WIS 14 (+2) CHA 5 (-3) Senses  passive Perception 12 Languages  — Challenge  0 (10 XP) Actions Bite .  Melee Weapon Attack : +2 to hit', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage.'

