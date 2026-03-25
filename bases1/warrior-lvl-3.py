# bases1/warrior-lvl-3.py
"""
WarriorLvl3 creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warrior-lvl-3
"""
from creature_base import GlobalCreatureBaseClass


class WarriorLvl3(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - WarriorLvl3
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 13, 'CON': 14, 'INT': 10, 'WIS': 12, 'CHAR': 10, 'armor_class': 16, 'alignment': '- Armor Class  16 (chain shirt', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['martial_role', 'longsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def martial_role(self) -> str:
        """The warrior has one of the following traits of your choice:Attacker. The warrior gains a +2 bonus to attack rolls.Defender. The warrior gains the Protection reaction below.Second Wind. The warrior can"""
        return 'The warrior has one of the following traits of your choice:Attacker. The warrior gains a +2 bonus to attack rolls.Defender. The warrior gains the Protection reaction below.Second Wind. The warrior can'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target. Hit: 5 (1d8 + 1) piercing damage."""
        return 'Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target. Hit: 5 (1d8 + 1) piercing damage.'

