# bases1/quipper.py
"""
Quipper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quipper
"""
from creature_base import GlobalCreatureBaseClass


class Quipper(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Quipper
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 16, 'CON': 9, 'INT': 1, 'WIS': 7, 'CHAR': 2, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  1 (1d4 - 1) Speed  0 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blood_frenzy', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blood_frenzy(self) -> str:
        """The quipper has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The quipper can breathe only underwater."""
        return "The quipper has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The quipper can breathe only underwater."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage.'

