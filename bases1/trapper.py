# bases1/trapper.py
"""
Trapper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=trapper
"""
from creature_base import GlobalCreatureBaseClass


class Trapper(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - Trapper
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 17, 'INT': 2, 'WIS': 13, 'CHAR': 4, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  68 (8d10 + 24) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'smother']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """If the trapper is motionless on a floor, wall, or ceiling at the start of combat, it has advantage on its initiative roll. Moreover, if a creature hasn't observed the trapper move or act, that creatur"""
        return "If the trapper is motionless on a floor, wall, or ceiling at the start of combat, it has advantage on its initiative roll. Moreover, if a creature hasn't observed the trapper move or act, that creatur"

    def smother_attack(self) -> str:
        """One Large or smaller creature within 10 feet of the trapper must succeed on a DC 13 Dexterity saving throw or be grappled (escape DC 14). Until the grapple ends, the target takes 13 (3d6 + 3) bludgeoning damage plus 3 (1d6) acid damage at the start of each of its turns. While grappled in this way, the target is restrained, blinded, and deprived of air. The trapper can smother only one creature at a time."""
        return 'One Large or smaller creature within 10 feet of the trapper must succeed on a DC 13 Dexterity saving throw or be grappled (escape DC 14). Until the grapple ends, the target takes 13 (3d6 + 3) bludgeoning damage plus 3 (1d6) acid damage at the start of each of its turns. While grappled in this way, the target is restrained, blinded, and deprived of air. The trapper can smother only one creature at a time.'

