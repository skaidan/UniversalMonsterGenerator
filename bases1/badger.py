# bases1/badger.py
"""
Badger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=badger
"""
from creature_base import GlobalCreatureBaseClass


class Badger(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Badger
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 3, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 11, 'CON': 12, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 10, 'alignment': 'unaligned Armor Class', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'challenge': '0', 'saving_throws': None, 'skills': None, 'damage_resistances': None, 'damage_immunities': None, 'condition_immunities': None, 'senses': 'darkvision 30 ft., passive Perception 11', 'languages': None, 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The badger has advantage on Wisdom (Perception) checks that rely on smell."""
        return 'The badger has advantage on Wisdom (Perception) checks that rely on smell.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage.'

