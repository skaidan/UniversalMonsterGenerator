# bases1/death-knight.py
"""
DeathKnight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-knight
"""
from creature_base import GlobalCreatureBaseClass


class DeathKnight(GlobalCreatureBaseClass):
    """
    Medium undead creature - DeathKnight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 180, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 11, 'CON': 20, 'INT': 12, 'WIS': 16, 'CHAR': 18, 'armor_class': 20, 'alignment': 'chaotic evil Armor Class  20 (plate', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'longsword', 'hellfire_orb_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The death knight has advantage on saving throws against spells and other magical effects.Marshal Undead. Unless the death knight is incapacitated, it and undead creatures of its choice within 60 feet """
        return 'The death knight has advantage on saving throws against spells and other magical effects.Marshal Undead. Unless the death knight is incapacitated, it and undead creatures of its choice within 60 feet '

    def multiattack_attack(self) -> str:
        """The death knight makes three longsword attacks."""
        return 'The death knight makes three longsword attacks.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage, or 10 (1d10 + 5) slashing damage if used with two hands, plus 18 (4d8) necrotic damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage, or 10 (1d10 + 5) slashing damage if used with two hands, plus 18 (4d8) necrotic damage.'

    def hellfire_orb_(1/day)_attack(self) -> str:
        """The death knight hurls a magical ball of fire that explodes at a point it can see within 120 feet of it. Each creature in a 20-foot-radius sphere centered on that point must make a DC 18 Dexterity saving throw. The sphere spreads around corners. A creature takes 35 (10d6) fire damage and 35 (10d6) necrotic damage on a failed save, or half as much damage on a successful one."""
        return 'The death knight hurls a magical ball of fire that explodes at a point it can see within 120 feet of it. Each creature in a 20-foot-radius sphere centered on that point must make a DC 18 Dexterity saving throw. The sphere spreads around corners. A creature takes 35 (10d6) fire damage and 35 (10d6) necrotic damage on a failed save, or half as much damage on a successful one.'

