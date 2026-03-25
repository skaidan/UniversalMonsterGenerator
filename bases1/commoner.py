# bases1/commoner.py
"""
Commoner creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=commoner
"""
from creature_base import GlobalCreatureBaseClass


class Commoner(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Commoner
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 4, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 10, 'CON': 10, 'INT': 10, 'WIS': 10, 'CHAR': 10, 'armor_class': 10, 'alignment': 'any alignment Armor Class  10 Hit Points  4 (1d8) Speed  30 ft. STR 10 (+0) DEX 10 (+0) CON 10 (+0) INT 10 (+0) WIS 10 (+0) CHA 10 (+0) Senses  passive Perception 10 Languages  any one language (usually Common) Challenge  0 (10 XP) Actions Club .  Melee Weapon Attack : +2 to hit', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['club']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def club_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.'

