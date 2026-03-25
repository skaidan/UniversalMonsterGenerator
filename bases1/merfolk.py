# bases1/merfolk.py
"""
Merfolk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merfolk
"""
from creature_base import GlobalCreatureBaseClass


class Merfolk(GlobalCreatureBaseClass):
    """
    Medium humanoid (Merfolk) creature - Merfolk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 13, 'CON': 12, 'INT': 11, 'WIS': 11, 'CHAR': 12, 'armor_class': 11, 'alignment': 'neutral Armor Class  11 Hit Points  11 (2d8 + 2) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Merfolk)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'spear']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The merfolk can breathe air and water."""
        return 'The merfolk can breathe air and water.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 3 (1d6) piercing damage, or 4 (1d8) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 3 (1d6) piercing damage, or 4 (1d8) piercing damage if used with two hands to make a melee attack.'

