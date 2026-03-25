# bases1/red-dragon-wyrmling.py
"""
RedDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=red-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class RedDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Chromatic) creature - RedDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 10, 'CON': 17, 'INT': 12, 'WIS': 11, 'CHAR': 15, 'armor_class': 17, 'alignment': 'chaotic evil Armor Class  17 (natural armor) Hit Points  75 (10d8 + 30) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'fire_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage plus 3 (1d6) fire damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage plus 3 (1d6) fire damage.'

    def fire_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC 13 Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC 13 Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one.'

