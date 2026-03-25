# bases1/minor-earth-elemental.py
"""
MinorEarthElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minor-earth-elemental
"""
from creature_base import GlobalCreatureBaseClass


class MinorEarthElemental(GlobalCreatureBaseClass):
    """
    Small elemental creature - MinorEarthElemental
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 6, 'CON': 16, 'INT': 3, 'WIS': 10, 'CHAR': 5, 'armor_class': 15, 'alignment': 'neutral Armor Class  15 (natural qrmor) Hit Points  60 (8d8 + 24) Speed  10 ft.', 'legendary': False, 'size': 'Small', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['downhill_roller', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def downhill_roller(self) -> str:
        """The elemental's walking speed increases to 30 while moving downhill. If it moves at least 15 feet straight towards a target and then hits it with a slam attack on the same turn, the target takes an ex"""
        return "The elemental's walking speed increases to 30 while moving downhill. If it moves at least 15 feet straight towards a target and then hits it with a slam attack on the same turn, the target takes an ex"

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) bludgeoning damage.'

