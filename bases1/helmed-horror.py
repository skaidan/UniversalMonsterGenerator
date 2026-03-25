# bases1/helmed-horror.py
"""
HelmedHorror creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=helmed-horror
"""
from creature_base import GlobalCreatureBaseClass


class HelmedHorror(GlobalCreatureBaseClass):
    """
    Medium construct creature - HelmedHorror
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 16, 'INT': 10, 'WIS': 10, 'CHAR': 10, 'armor_class': 20, 'alignment': 'neutral Armor Class  20 (plate', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'longsword']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The helmed horror has advantage on saving throws against spells and other magical effects.Spell Immunity. The helmed horror is immune to three spells chosen by its creator. Typical immunities include """
        return 'The helmed horror has advantage on saving throws against spells and other magical effects.Spell Immunity. The helmed horror is immune to three spells chosen by its creator. Typical immunities include '

    def multiattack_attack(self) -> str:
        """The helmed horror makes two longsword attacks."""
        return 'The helmed horror makes two longsword attacks.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands.'

