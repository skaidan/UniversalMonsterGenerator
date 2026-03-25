# bases1/bandit-captain.py
"""
BanditCaptain creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bandit-captain
"""
from creature_base import GlobalCreatureBaseClass


class BanditCaptain(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - BanditCaptain
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 65, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 16, 'CON': 14, 'INT': 14, 'WIS': 11, 'CHAR': 14, 'armor_class': 15, 'alignment': 'any non-lawful alignment Armor Class  15 (studded leather) Hit Points  65 (10d8 + 20) Speed  30 ft. STR 15 (+2) DEX 16 (+3) CON 14 (+2) INT 14 (+2) WIS 11 (+0) CHA 14 (+2) Saving Throws  Str +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'scimitar', 'dagger', 'parry']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The captain makes three melee attacks: two with its scimitar and one with its dagger. Or the captain makes two ranged attacks with its daggers."""
        return 'The captain makes three melee attacks: two with its scimitar and one with its dagger. Or the captain makes two ranged attacks with its daggers.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage.'

    def parry_attack(self) -> str:
        """The captain adds 2 to its AC against one melee attack that would hit it. To do so, the captain must see the attacker and be wielding a melee weapon."""
        return 'The captain adds 2 to its AC against one melee attack that would hit it. To do so, the captain must see the attacker and be wielding a melee weapon.'

