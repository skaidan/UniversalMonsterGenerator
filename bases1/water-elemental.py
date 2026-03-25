# bases1/water-elemental.py
"""
WaterElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=water-elemental
"""
from creature_base import GlobalCreatureBaseClass


class WaterElemental(GlobalCreatureBaseClass):
    """
    Large elemental creature - WaterElemental
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 114, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 18, 'INT': 5, 'WIS': 10, 'CHAR': 8, 'armor_class': 14, 'alignment': 'neutral Armor Class  14 (natural armor) Hit Points  114 (12d10 + 48) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['water_form', 'multiattack', 'slam', 'whelm_(recharge_4-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def water_form(self) -> str:
        """The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.Freeze. If the elemental takes cold damage, it partially freez"""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.Freeze. If the elemental takes cold damage, it partially freez"

    def multiattack_attack(self) -> str:
        """The elemental makes two slam attacks."""
        return 'The elemental makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.'

    def whelm_(recharge_4-6)_attack(self) -> str:
        """Each creature in the elemental's space must make a DC 15 Strength saving throw. On a failure, a target takes 13 (2d8 + 4) bludgeoning damage. If it is Large or smaller, it is also grappled (escape DC 14). Until this grapple ends, the target is restrained and unable to breathe unless it can breathe water. If the saving throw is successful, the target is pushed out of the elemental's space. The elemental can grapple one Large creature or up to two Medium or smaller creatures at one time. At the start of each of the elemental's turns, each target grappled by it takes 13 (2d8 + 4) bludgeoning damage. A creature within 5 feet of the elemental can pull a creature or object out of it by taking an action to make a DC 14 Strength check and succeeding."""
        return "Each creature in the elemental's space must make a DC 15 Strength saving throw. On a failure, a target takes 13 (2d8 + 4) bludgeoning damage. If it is Large or smaller, it is also grappled (escape DC 14). Until this grapple ends, the target is restrained and unable to breathe unless it can breathe water. If the saving throw is successful, the target is pushed out of the elemental's space. The elemental can grapple one Large creature or up to two Medium or smaller creatures at one time. At the start of each of the elemental's turns, each target grappled by it takes 13 (2d8 + 4) bludgeoning damage. A creature within 5 feet of the elemental can pull a creature or object out of it by taking an action to make a DC 14 Strength check and succeeding."

