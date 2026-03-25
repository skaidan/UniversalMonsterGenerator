# bases1/vulture.py
"""
Vulture creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vulture
"""
from creature_base import GlobalCreatureBaseClass


class Vulture(GlobalCreatureBaseClass):
    """
    Medium beast creature - Vulture
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 5, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 10, 'CON': 13, 'INT': 2, 'WIS': 12, 'CHAR': 4, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  5 (1d8 + 1) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight_and_smell', 'beak']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight_and_smell(self) -> str:
        """The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies"""
        return "The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies"

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage.'

