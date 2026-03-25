# bases1/veteran.py
"""
Veteran creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=veteran
"""
from creature_base import GlobalCreatureBaseClass


class Veteran(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Veteran
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 13, 'CON': 14, 'INT': 10, 'WIS': 11, 'CHAR': 10, 'armor_class': 17, 'alignment': 'any alignment Armor Class  17 (splint) Hit Points  58 (9d8 + 18) Speed  30 ft. STR 16 (+3) DEX 13 (+1) CON 14 (+2) INT 10 (+0) WIS 11 (+0) CHA 10 (+0) Skills  Athletics +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'longsword', 'shortsword', 'heavy_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword attack."""
        return 'The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword attack.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def heavy_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +3 to hit, range 100/400 ft., one target. Hit: 6 (1d10 + 1) piercing damage."""
        return 'Ranged Weapon Attack: +3 to hit, range 100/400 ft., one target. Hit: 6 (1d10 + 1) piercing damage.'

