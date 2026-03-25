# bases1/crab.py
"""
Crab creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crab
"""
from creature_base import GlobalCreatureBaseClass


class Crab(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Crab
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 2, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 11, 'CON': 10, 'INT': 1, 'WIS': 8, 'CHAR': 2, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 (natural armor) Hit Points  2 (1d4) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The crab can breathe air and water."""
        return 'The crab can breathe air and water.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage."""
        return 'Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage.'

