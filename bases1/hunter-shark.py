# bases1/hunter-shark.py
"""
HunterShark creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hunter-shark
"""
from creature_base import GlobalCreatureBaseClass


class HunterShark(GlobalCreatureBaseClass):
    """
    Large beast creature - HunterShark
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 15, 'INT': 1, 'WIS': 10, 'CHAR': 4, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  45 (6d10 + 12) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blood_frenzy', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blood_frenzy(self) -> str:
        """The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The shark can breathe only underwater."""
        return "The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The shark can breathe only underwater."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage.'

