# bases1/black-dragon-wyrmling.py
"""
BlackDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=black-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class BlackDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Chromatic) creature - BlackDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 13, 'INT': 10, 'WIS': 11, 'CHAR': 13, 'armor_class': 17, 'alignment': 'chaotic evil Armor Class  17 (natural armor) Hit Points  33 (6d8 + 6) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'bite', 'acid_breath_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The dragon can breathe air and water."""
        return 'The dragon can breathe air and water.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 2 (1d4) acid damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 2 (1d4) acid damage.'

    def acid_breath_(recharge_5–6)_attack(self) -> str:
        """The dragon exhales acid in a 15-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 22 (5d8) acid damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales acid in a 15-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 22 (5d8) acid damage on a failed save, or half as much damage on a successful one.'

