# bases1/camel.py
"""
Camel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=camel
"""
from creature_base import GlobalCreatureBaseClass


class Camel(GlobalCreatureBaseClass):
    """
    Large beast creature - Camel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 15, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 8, 'CON': 14, 'INT': 2, 'WIS': 8, 'CHAR': 5, 'armor_class': 9, 'alignment': 'unaligned Armor Class  9 Hit Points  15 (2d10 + 4) Speed  50 ft. STR 16 (+3) DEX 8 (-1) CON 14 (+2) INT 2 (-4) WIS 8 (-1) CHA 5 (-3) Senses  passive Perception 9 Languages  — Challenge  1/8 (25 XP) Actions Bite .  Melee Weapon Attack : +5 to hit', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.'

