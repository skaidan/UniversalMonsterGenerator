# bases1/piercer.py
"""
Piercer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=piercer
"""
from creature_base import GlobalCreatureBaseClass


class Piercer(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - Piercer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 13, 'CON': 16, 'INT': 1, 'WIS': 7, 'CHAR': 3, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  22 (3d8 + 9) Speed  5 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'drop']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the piercer remains motionless on the ceiling, it is indistinguishable from a normal stalactite.Spider Climb. The piercer can climb difficult surfaces, including upside down on ceilings, without"""
        return 'While the piercer remains motionless on the ceiling, it is indistinguishable from a normal stalactite.Spider Climb. The piercer can climb difficult surfaces, including upside down on ceilings, without'

    def drop_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, one creature directly underneath the piercer. Hit: 3 (1d6) piercing damage per 10 feet fallen, up to 21 (6d6). Miss: The piercer takes half the normal falling damage for the distance fallen."""
        return 'Melee Weapon Attack: +3 to hit, one creature directly underneath the piercer. Hit: 3 (1d6) piercing damage per 10 feet fallen, up to 21 (6d6). Miss: The piercer takes half the normal falling damage for the distance fallen.'

