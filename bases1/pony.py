# bases1/pony.py
"""
Pony creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pony
"""
from creature_base import GlobalCreatureBaseClass


class Pony(GlobalCreatureBaseClass):
    """
    Medium beast creature - Pony
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 13, 'INT': 2, 'WIS': 11, 'CHAR': 7, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  11 (2d8 + 2) Speed  40 ft. STR 15 (+2) DEX 10 (+0) CON 13 (+1) INT 2 (-4) WIS 11 (+0) CHA 7 (-2) Senses  passive Perception 10 Languages  — Challenge  1/8 (25 XP) Actions Hooves .  Melee Weapon Attack : +4 to hit', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) bludgeoning damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) bludgeoning damage.'

