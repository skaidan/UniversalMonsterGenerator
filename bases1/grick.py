# bases1/grick.py
"""
Grick creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grick
"""
from creature_base import GlobalCreatureBaseClass


class Grick(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - Grick
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 11, 'INT': 3, 'WIS': 14, 'CHAR': 5, 'armor_class': 14, 'alignment': 'neutral Armor Class  14 (natural armor) Hit Points  27 (6d8) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['stone_camouflage', 'multiattack', 'tentacles', 'beak']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def stone_camouflage(self) -> str:
        """The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."""
        return 'The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.'

    def multiattack_attack(self) -> str:
        """The grick makes one attack with its tentacles. If that attack hits, the grick can make one beak attack against the same target."""
        return 'The grick makes one attack with its tentacles. If that attack hits, the grick can make one beak attack against the same target.'

    def tentacles_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

