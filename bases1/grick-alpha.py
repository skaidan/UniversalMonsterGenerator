# bases1/grick-alpha.py
"""
GrickAlpha creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grick-alpha
"""
from creature_base import GlobalCreatureBaseClass


class GrickAlpha(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - GrickAlpha
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 16, 'CON': 15, 'INT': 4, 'WIS': 14, 'CHAR': 9, 'armor_class': 18, 'alignment': 'neutral Armor Class  18 (natural armor) Hit Points  75 (10d10 + 20) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['stone_camouflage', 'multiattack', 'tail', 'tentacles', 'beak']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def stone_camouflage(self) -> str:
        """The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."""
        return 'The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.'

    def multiattack_attack(self) -> str:
        """The grick makes two attacks: one with its tail and one with its tentacles. If it hits with its tentacles, the grick can make one beak attack against the same target."""
        return 'The grick makes two attacks: one with its tail and one with its tentacles. If it hits with its tentacles, the grick can make one beak attack against the same target.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

    def tentacles_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 22 (4d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 22 (4d8 + 4) slashing damage.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) piercing damage.'

