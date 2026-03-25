# bases1/orc-war-chief.py
"""
OrcWarChief creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-war-chief
"""
from creature_base import GlobalCreatureBaseClass


class OrcWarChief(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - OrcWarChief
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 12, 'CON': 18, 'INT': 11, 'WIS': 11, 'CHAR': 16, 'armor_class': 16, 'alignment': 'chaotic evil Armor Class  16 (chain mail) Hit Points  93 (11d8 + 44) Speed  30 ft. STR 18 (+4) DEX 12 (+1) CON 18 (+4) INT 11 (+0) WIS 11 (+0) CHA 16 (+3) Saving Throws  Str +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aggressive', 'multiattack', 'greataxe', 'spear', 'battle_cry_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aggressive(self) -> str:
        """As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruumsh's Fury. The orc deals an extra 4 (1d8) damage when it hits with a weapon attack (included in the a"""
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruumsh's Fury. The orc deals an extra 4 (1d8) damage when it hits with a weapon attack (included in the a"

    def multiattack_attack(self) -> str:
        """The orc makes two attacks with its greataxe or its spear."""
        return 'The orc makes two attacks with its greataxe or its spear.'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 15 (1d12 + 4 plus 1d8) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 15 (1d12 + 4 plus 1d8) slashing damage.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 12 (1d6 + 4 plus 1d8) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 12 (1d6 + 4 plus 1d8) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack.'

    def battle_cry_(1/day)_attack(self) -> str:
        """Each creature of the war chief's choice that is within 30 feet of it, can hear it, and not already affected by Battle Cry gain advantage on attack rolls until the start of the war chief's next turn. The war chief can then make one attack as a bonus action."""
        return "Each creature of the war chief's choice that is within 30 feet of it, can hear it, and not already affected by Battle Cry gain advantage on attack rolls until the start of the war chief's next turn. The war chief can then make one attack as a bonus action."

