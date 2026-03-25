# bases1/draft-horse.py
"""
DraftHorse creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draft-horse
"""
from creature_base import GlobalCreatureBaseClass


class DraftHorse(GlobalCreatureBaseClass):
    """
    Large beast creature - DraftHorse
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 12, 'INT': 2, 'WIS': 11, 'CHAR': 7, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  19 (3d10 + 3) Speed  40 ft. STR 18 (+4) DEX 10 (+0) CON 12 (+1) INT 2 (-4) WIS 11 (+0) CHA 7 (-2) Senses  passive Perception 10 Languages  — Challenge  1/4 (50 XP) Actions Hooves .  Melee Weapon Attack : +6 to hit', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.'

