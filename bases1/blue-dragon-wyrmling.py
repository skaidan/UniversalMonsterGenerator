# bases1/blue-dragon-wyrmling.py
"""
BlueDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blue-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class BlueDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Chromatic) creature - BlueDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 15, 'INT': 12, 'WIS': 11, 'CHAR': 15, 'armor_class': 17, 'alignment': 'lawful evil Armor Class  17 (natural armor) Hit Points  52 (8d8 + 16) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'lightning_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 3 (1d6) lightning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 3 (1d6) lightning damage.'

    def lightning_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales lightning in a 30-foot line that is 5 feet wide. Each creature in that line must make a DC 12 Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales lightning in a 30-foot line that is 5 feet wide. Each creature in that line must make a DC 12 Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one.'

