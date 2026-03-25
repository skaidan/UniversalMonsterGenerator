# bases1/giant-badger.py
"""
GiantBadger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-badger
"""
from creature_base import GlobalCreatureBaseClass


class GiantBadger(GlobalCreatureBaseClass):
    """
    Medium beast creature - GiantBadger
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 10, 'CON': 15, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  13 (2d8 + 4) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'multiattack', 'bite', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The badger has advantage on Wisdom (Perception) checks that rely on smell."""
        return 'The badger has advantage on Wisdom (Perception) checks that rely on smell.'

    def multiattack_attack(self) -> str:
        """The badger makes two attacks: one with its bite and one with its claws."""
        return 'The badger makes two attacks: one with its bite and one with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage.'

