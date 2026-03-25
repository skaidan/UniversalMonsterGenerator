# bases1/ochre-jelly.py
"""
OchreJelly creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ochre-jelly
"""
from creature_base import GlobalCreatureBaseClass


class OchreJelly(GlobalCreatureBaseClass):
    """
    Large ooze creature - OchreJelly
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 6, 'CON': 14, 'INT': 2, 'WIS': 6, 'CHAR': 1, 'armor_class': 8, 'alignment': 'unaligned Armor Class  8 Hit Points  45 (6d10 + 12) Speed  10 ft.', 'legendary': False, 'size': 'Large', 'type': 'ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amorphous', 'pseudopod']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amorphous(self) -> str:
        """The jelly can move through a space as narrow as 1 inch wide without squeezing.Spider Climb. The jelly can climb difficult surfaces, including upside down on ceilings, without needing to make an abilit"""
        return 'The jelly can move through a space as narrow as 1 inch wide without squeezing.Spider Climb. The jelly can climb difficult surfaces, including upside down on ceilings, without needing to make an abilit'

    def pseudopod_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage plus 3 (1d6) acid damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage plus 3 (1d6) acid damage.'

