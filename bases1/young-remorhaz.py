# bases1/young-remorhaz.py
"""
YoungRemorhaz creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-remorhaz
"""
from creature_base import GlobalCreatureBaseClass


class YoungRemorhaz(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - YoungRemorhaz
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 17, 'INT': 3, 'WIS': 10, 'CHAR': 4, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  93 (11d10 + 33) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['heated_body', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def heated_body(self) -> str:
        """A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage."""
        return 'A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 20 (3d10 + 4) piercing damage plus 7 (2d6) fire damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 20 (3d10 + 4) piercing damage plus 7 (2d6) fire damage.'

