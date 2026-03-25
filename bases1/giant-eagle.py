# bases1/giant-eagle.py
"""
GiantEagle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-eagle
"""
from creature_base import GlobalCreatureBaseClass


class GiantEagle(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantEagle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 17, 'CON': 13, 'INT': 8, 'WIS': 14, 'CHAR': 10, 'armor_class': 13, 'alignment': 'neutral good Armor Class', 'legendary': False, 'size': 'Large', 'type': 'beast', 'challenge': '0', 'saving_throws': None, 'skills': 'Perception +4', 'damage_resistances': None, 'damage_immunities': None, 'condition_immunities': None, 'senses': 'passive Perception 14', 'languages': None, 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'multiattack', 'beak', 'talons']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The eagle has advantage on Wisdom (Perception) checks that rely on sight."""
        return 'The eagle has advantage on Wisdom (Perception) checks that rely on sight.'

    def multiattack_attack(self) -> str:
        """The eagle makes two attacks: one with its beak and one with its talons."""
        return 'The eagle makes two attacks: one with its beak and one with its talons.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def talons_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage.'

