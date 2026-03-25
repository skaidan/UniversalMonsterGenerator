# bases1/panther.py
"""
Panther creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=panther
"""
from creature_base import GlobalCreatureBaseClass


class Panther(GlobalCreatureBaseClass):
    """
    Medium beast creature - Panther
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 15, 'CON': 10, 'INT': 3, 'WIS': 14, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  13 (3d8) Speed  50 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The panther has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the panther moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn"""
        return 'The panther has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the panther moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

