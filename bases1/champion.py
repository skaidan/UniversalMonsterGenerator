# bases1/champion.py
"""
Champion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=champion
"""
from creature_base import GlobalCreatureBaseClass


class Champion(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - Champion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 143, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 15, 'CON': 14, 'INT': 10, 'WIS': 14, 'CHAR': 12, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  143 (22d8 + 44) Speed  30 ft. STR 20 (+5) DEX 15 (+2) CON 14 (+2) INT 10 (+0) WIS 14 (+2) CHA 12 (+1) Saving Throws  Str +9', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['indomitable_(2/day)', 'multiattack', 'greatsword', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def indomitable_(2/day)(self) -> str:
        """The champion rerolls a failed saving throw."""
        return 'The champion rerolls a failed saving throw.'

    def multiattack_attack(self) -> str:
        """The champion makes three Greatsword or Shortbow attacks."""
        return 'The champion makes three Greatsword or Shortbow attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage, plus 7 (2d6) slashing damage if the champion has more than half of its total hit points remaining."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage, plus 7 (2d6) slashing damage if the champion has more than half of its total hit points remaining.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage, plus 7 (2d6) piercing damage if the champion has more than half of its total hit points remaining."""
        return 'Ranged Weapon Attack: +6 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage, plus 7 (2d6) piercing damage if the champion has more than half of its total hit points remaining.'

