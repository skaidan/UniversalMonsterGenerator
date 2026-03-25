# bases1/assassin.py
"""
Assassin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=assassin
"""
from creature_base import GlobalCreatureBaseClass


class Assassin(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Assassin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 78, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 14, 'INT': 13, 'WIS': 11, 'CHAR': 10, 'armor_class': 15, 'alignment': 'any non-good alignment Armor Class  15 (studded leather) Hit Points  78 (12d8 + 24) Speed  30 ft. STR 11 (+0) DEX 16 (+3) CON 14 (+2) INT 13 (+1) WIS 11 (+0) CHA 10 (+0) Saving Throws  Dex +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['assassinate', 'multiattack', 'shortsword', 'light_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def assassinate(self) -> str:
        """During its first turn, the assassin has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critical hit.Evasion. If """
        return "During its first turn, the assassin has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critical hit.Evasion. If "

    def multiattack_attack(self) -> str:
        """The assassin makes two shortsword attacks."""
        return 'The assassin makes two shortsword attacks.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one.'

    def light_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 80/320 ft., one target. Hit: 7 (1d8 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Ranged Weapon Attack: +6 to hit, range 80/320 ft., one target. Hit: 7 (1d8 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one.'

