# bases1/air-elemental.py
"""
AirElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=air-elemental
"""
from creature_base import GlobalCreatureBaseClass


class AirElemental(GlobalCreatureBaseClass):
    """
    Large elemental creature - AirElemental
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 20, 'CON': 14, 'INT': 6, 'WIS': 10, 'CHAR': 6, 'armor_class': 15, 'alignment': 'neutral Armor Class  15 Hit Points  90 (12d10 + 24) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['air_form', 'multiattack', 'slam', 'whirlwind_(recharge_4-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def air_form(self) -> str:
        """The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."

    def multiattack_attack(self) -> str:
        """The elemental makes two slam attacks."""
        return 'The elemental makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage.'

    def whirlwind_(recharge_4-6)_attack(self) -> str:
        """Each creature in the elemental's space must make a DC 13 Strength saving throw. On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up 20 feet away from the elemental in a random direction and knocked prone. If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 13 Dexterity saving throw or take the same damage and be knocked prone. If the saving throw is successful, the target takes half the bludgeoning damage and isn't flung away or knocked prone."""
        return "Each creature in the elemental's space must make a DC 13 Strength saving throw. On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up 20 feet away from the elemental in a random direction and knocked prone. If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 13 Dexterity saving throw or take the same damage and be knocked prone. If the saving throw is successful, the target takes half the bludgeoning damage and isn't flung away or knocked prone."

