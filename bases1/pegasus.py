# bases1/pegasus.py
"""
Pegasus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pegasus
"""
from creature_base import GlobalCreatureBaseClass


class Pegasus(GlobalCreatureBaseClass):
    """
    Large celestial creature - Pegasus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 59, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 10, 'WIS': 15, 'CHAR': 13, 'armor_class': 12, 'alignment': 'chaotic good Armor Class  12 Hit Points  59 (7d10 + 21) Speed  60 ft.', 'legendary': False, 'size': 'Large', 'type': 'celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

