# bases1/earth-elemental.py
"""
EarthElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=earth-elemental
"""
from creature_base import GlobalCreatureBaseClass


class EarthElemental(GlobalCreatureBaseClass):
    """
    Large elemental creature - EarthElemental
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 126, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 8, 'CON': 20, 'INT': 5, 'WIS': 10, 'CHAR': 5, 'armor_class': 17, 'alignment': 'neutral Armor Class  17 (natural armor) Hit Points  126 (12d10 + 60) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['earth_glide', 'multiattack', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def earth_glide(self) -> str:
        """The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through.Siege Monster. The elemental deals double damage to o"""
        return "The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through.Siege Monster. The elemental deals double damage to o"

    def multiattack_attack(self) -> str:
        """The elemental makes two slam attacks."""
        return 'The elemental makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage.'

