# bases1/beast-of-the-land.py
"""
BeastOfTheLand creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=beast-of-the-land
"""
from creature_base import GlobalCreatureBaseClass


class BeastOfTheLand(GlobalCreatureBaseClass):
    """
    Medium beast creature - BeastOfTheLand
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 15, 'INT': 8, 'WIS': 14, 'CHAR': 11, 'armor_class': 13, 'alignment': '- Armor Class  13 + PB (natural armor) Hit Points  5 + five times your ranger level (the beast has a number of Hit Dice [d8s] equal to your ranger level) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'maul']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the beast moves at least 20 feet straight toward a target and then hits it with a maul attack on the same turn, the target takes an extra 1d6 slashing damage. If the target is a creature, it must s"""
        return 'If the beast moves at least 20 feet straight toward a target and then hits it with a maul attack on the same turn, the target takes an extra 1d6 slashing damage. If the target is a creature, it must s'

    def maul_attack(self) -> str:
        """Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target. Hit: 1d8 + 2 + PB slashing damage."""
        return 'Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target. Hit: 1d8 + 2 + PB slashing damage.'

