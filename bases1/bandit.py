# bases1/bandit.py
"""
Bandit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bandit
"""
from creature_base import GlobalCreatureBaseClass


class Bandit(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Bandit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 12, 'CON': 12, 'INT': 10, 'WIS': 10, 'CHAR': 10, 'armor_class': 12, 'alignment': 'any non-lawful alignment Armor Class  12 (leather armor) Hit Points  11 (2d8 + 2) Speed  30 ft. STR 11 (+0) DEX 12 (+1) CON 12 (+1) INT 10 (+0) WIS 10 (+0) CHA 10 (+0) Senses  passive Perception 10 Languages  any one language (usually Common) Challenge  1/8 (25 XP) Actions Scimitar .  Melee Weapon Attack : +3 to hit', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['scimitar', 'light_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.'

    def light_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +3 to hit, range 80 ft./320 ft., one target. Hit: 5 (1d8 + 1) piercing damage."""
        return 'Ranged Weapon Attack: +3 to hit, range 80 ft./320 ft., one target. Hit: 5 (1d8 + 1) piercing damage.'

