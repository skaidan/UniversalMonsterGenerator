# bases1/knight.py
"""
Knight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=knight
"""
from creature_base import GlobalCreatureBaseClass


class Knight(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Knight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 14, 'INT': 11, 'WIS': 11, 'CHAR': 15, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  52 (8d8 + 16) Speed  30 ft. STR 16 (+3) DEX 11 (+0) CON 14 (+2) INT 11 (+0) WIS 11 (+0) CHA 15 (+2) Saving Throws  Con +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['brave', 'multiattack', 'greatsword', 'heavy_crossbow', 'leadership_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def brave(self) -> str:
        """The knight has advantage on saving throws against being frightened."""
        return 'The knight has advantage on saving throws against being frightened.'

    def multiattack_attack(self) -> str:
        """The knight makes two melee attacks."""
        return 'The knight makes two melee attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage.'

    def heavy_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +2 to hit, range 100/400 ft., one target. Hit: 5 (1d10) piercing damage."""
        return 'Ranged Weapon Attack: +2 to hit, range 100/400 ft., one target. Hit: 5 (1d10) piercing damage.'

    def leadership_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """For 1 minute, the knight can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the knight. A creature can benefit from only one Leadership die at a time. This effect ends if the knight is incapacitated."""
        return 'For 1 minute, the knight can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the knight. A creature can benefit from only one Leadership die at a time. This effect ends if the knight is incapacitated.'

