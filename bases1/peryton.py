# bases1/peryton.py
"""
Peryton creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=peryton
"""
from creature_base import GlobalCreatureBaseClass


class Peryton(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - Peryton
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 13, 'INT': 9, 'WIS': 12, 'CHAR': 10, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 (natural armor) Hit Points  33 (6d8 + 6) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['dive_attack', 'multiattack', 'gore', 'talons']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dive_attack(self) -> str:
        """If the peryton is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 9 (2d8) damage to the target.Flyby. The peryton does"""
        return 'If the peryton is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 9 (2d8) damage to the target.Flyby. The peryton does'

    def multiattack_attack(self) -> str:
        """The peryton makes one gore attack and one talon attack."""
        return 'The peryton makes one gore attack and one talon attack.'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage.'

    def talons_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) piercing damage.'

