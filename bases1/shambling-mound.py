# bases1/shambling-mound.py
"""
ShamblingMound creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shambling-mound
"""
from creature_base import GlobalCreatureBaseClass


class ShamblingMound(GlobalCreatureBaseClass):
    """
    Large plant creature - ShamblingMound
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 8, 'CON': 16, 'INT': 5, 'WIS': 10, 'CHAR': 5, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  136 (16d10 + 48) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['lightning_absorption', 'multiattack', 'slam', 'engulf']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def lightning_absorption(self) -> str:
        """Whenever the shambling mound is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt."""
        return 'Whenever the shambling mound is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt.'

    def multiattack_attack(self) -> str:
        """The shambling mound makes two slam attacks. If both attacks hit a Medium or smaller target, the target is grappled (escape DC 14), and the shambling mound uses its Engulf on it."""
        return 'The shambling mound makes two slam attacks. If both attacks hit a Medium or smaller target, the target is grappled (escape DC 14), and the shambling mound uses its Engulf on it.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.'

    def engulf_attack(self) -> str:
        """The shambling mound engulfs a Medium or smaller creature grappled by it. The engulfed target is blinded, restrained, and unable to breathe, and it must succeed on a DC 14 Constitution saving throw at the start of each of the mound's turns or take 13 (2d8 + 4) bludgeoning damage. If the mound moves, the engulfed target moves with it. The mound can have only one creature engulfed at a time."""
        return "The shambling mound engulfs a Medium or smaller creature grappled by it. The engulfed target is blinded, restrained, and unable to breathe, and it must succeed on a DC 14 Constitution saving throw at the start of each of the mound's turns or take 13 (2d8 + 4) bludgeoning damage. If the mound moves, the engulfed target moves with it. The mound can have only one creature engulfed at a time."

