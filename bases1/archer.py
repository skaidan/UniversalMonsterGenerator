# bases1/archer.py
"""
Archer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=archer
"""
from creature_base import GlobalCreatureBaseClass


class Archer(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - Archer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 18, 'CON': 16, 'INT': 11, 'WIS': 13, 'CHAR': 10, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (studded leather) Hit Points  75 (10d8 + 30) Speed  30 ft. STR 11 (+0) DEX 18 (+4) CON 16 (+3) INT 11 (+0) WIS 13 (+1) CHA 10 (+0) Skills  Acrobatics +6', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'shortsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The archer makes two Shortsword or Longbow attacks."""
        return 'The archer makes two Shortsword or Longbow attacks.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 8 (1d8 + 4) piercing damage."""
        return 'Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 8 (1d8 + 4) piercing damage.'

