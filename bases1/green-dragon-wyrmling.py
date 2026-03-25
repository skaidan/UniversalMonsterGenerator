# bases1/green-dragon-wyrmling.py
"""
GreenDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=green-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class GreenDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Chromatic) creature - GreenDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 38, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 12, 'CON': 13, 'INT': 14, 'WIS': 11, 'CHAR': 13, 'armor_class': 17, 'alignment': 'lawful evil Armor Class  17 (natural armor) Hit Points  38 (7d8 + 7) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'bite', 'poison_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The dragon can breathe air and water."""
        return 'The dragon can breathe air and water.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 3 (1d6) poison damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 3 (1d6) poison damage.'

    def poison_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC 11 Constitution saving throw, taking 21 (6d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC 11 Constitution saving throw, taking 21 (6d6) poison damage on a failed save, or half as much damage on a successful one.'

