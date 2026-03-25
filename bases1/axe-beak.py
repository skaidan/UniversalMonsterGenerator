# bases1/axe-beak.py
"""
AxeBeak creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=axe-beak
"""
from creature_base import GlobalCreatureBaseClass


class AxeBeak(GlobalCreatureBaseClass):
    """
    Large beast creature - AxeBeak
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 12, 'CON': 12, 'INT': 2, 'WIS': 10, 'CHAR': 5, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  19 (3d10 + 3) Speed  50 ft. STR 14 (+2) DEX 12 (+1) CON 12 (+1) INT 2 (-4) WIS 10 (+0) CHA 5 (-3) Senses  passive Perception 10 Languages  — Challenge  1/4 (50 XP) Actions Beak .  Melee Weapon Attack : +4 to hit', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['beak']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage.'

