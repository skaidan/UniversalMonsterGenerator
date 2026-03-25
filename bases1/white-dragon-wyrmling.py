# bases1/white-dragon-wyrmling.py
"""
WhiteDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=white-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class WhiteDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Chromatic) creature - WhiteDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 10, 'CON': 14, 'INT': 5, 'WIS': 10, 'CHAR': 11, 'armor_class': 16, 'alignment': 'chaotic evil Armor Class  16 (natural armor) Hit Points  32 (5d8 + 10) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'cold_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 2 (1d4) cold damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 2 (1d4) cold damage.'

    def cold_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales an icy blast of hail in a 15-foot cone. Each creature in that area must make a DC 12 Constitution saving throw, taking 22 (5d8) cold damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales an icy blast of hail in a 15-foot cone. Each creature in that area must make a DC 12 Constitution saving throw, taking 22 (5d8) cold damage on a failed save, or half as much damage on a successful one.'

