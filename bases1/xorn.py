# bases1/xorn.py
"""
Xorn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=xorn
"""
from creature_base import GlobalCreatureBaseClass


class Xorn(GlobalCreatureBaseClass):
    """
    Medium elemental creature - Xorn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 73, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 22, 'INT': 11, 'WIS': 10, 'CHAR': 11, 'armor_class': 19, 'alignment': 'neutral Armor Class  19 (natural armor) Hit Points  73 (7d8 + 42) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['earth_glide', 'multiattack', 'claw', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def earth_glide(self) -> str:
        """The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't disturb the material it moves through.Stone Camouflage. The xorn has advantage on Dexterity (Stealth)"""
        return "The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't disturb the material it moves through.Stone Camouflage. The xorn has advantage on Dexterity (Stealth)"

    def multiattack_attack(self) -> str:
        """The xorn makes three claw attacks and one bite attack."""
        return 'The xorn makes three claw attacks and one bite attack.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (3d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (3d6 + 3) piercing damage.'

