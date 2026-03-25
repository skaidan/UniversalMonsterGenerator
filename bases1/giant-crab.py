# bases1/giant-crab.py
"""
GiantCrab creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-crab
"""
from creature_base import GlobalCreatureBaseClass


class GiantCrab(GlobalCreatureBaseClass):
    """
    Medium beast creature - GiantCrab
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 15, 'CON': 11, 'INT': 1, 'WIS': 9, 'CHAR': 3, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  13 (3d8) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The crab can breathe air and water."""
        return 'The crab can breathe air and water.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage, and the target is grappled (escape DC 11). The crab has two claws, each of which can grapple only one target."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage, and the target is grappled (escape DC 11). The crab has two claws, each of which can grapple only one target.'

