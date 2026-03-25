# bases1/dao.py
"""
Dao creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dao
"""
from creature_base import GlobalCreatureBaseClass


class Dao(GlobalCreatureBaseClass):
    """
    Large elemental creature - Dao
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 187, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 12, 'CON': 24, 'INT': 12, 'WIS': 13, 'CHAR': 14, 'armor_class': 18, 'alignment': 'neutral evil Armor Class  18 (natural armor) Hit Points  187 (15d10 + 105) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['earth_glide', 'multiattack', 'fist', 'maul']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def earth_glide(self) -> str:
        """The dao can burrow through nonmagical, unworked earth and stone. While doing so, the dao doesn't disturb the material it moves through.Elemental Demise. If the dao dies, its body disintegrates into cr"""
        return "The dao can burrow through nonmagical, unworked earth and stone. While doing so, the dao doesn't disturb the material it moves through.Elemental Demise. If the dao dies, its body disintegrates into cr"

    def multiattack_attack(self) -> str:
        """The dao makes two fist attacks or two maul attacks."""
        return 'The dao makes two fist attacks or two maul attacks.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage.'

    def maul_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 20 (4d6 + 6) bludgeoning damage. If the target is a Huge or smaller creature, it must succeed on a DC 18 Strength check or be knocked prone."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 20 (4d6 + 6) bludgeoning damage. If the target is a Huge or smaller creature, it must succeed on a DC 18 Strength check or be knocked prone.'

