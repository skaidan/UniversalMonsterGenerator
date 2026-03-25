# bases1/giant-vulture.py
"""
GiantVulture creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-vulture
"""
from creature_base import GlobalCreatureBaseClass


class GiantVulture(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantVulture
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 15, 'INT': 6, 'WIS': 12, 'CHAR': 7, 'armor_class': 10, 'alignment': 'neutral evil Armor Class  10 Hit Points  22 (3d10 + 6) Speed  10 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight_and_smell', 'multiattack', 'beak', 'talons']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight_and_smell(self) -> str:
        """The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies"""
        return "The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies"

    def multiattack_attack(self) -> str:
        """The vulture makes two attacks: one with its beak and one with its talons."""
        return 'The vulture makes two attacks: one with its beak and one with its talons.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage.'

    def talons_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage.'

