# bases1/reef-shark.py
"""
ReefShark creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=reef-shark
"""
from creature_base import GlobalCreatureBaseClass


class ReefShark(GlobalCreatureBaseClass):
    """
    Medium beast creature - ReefShark
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 13, 'CON': 13, 'INT': 1, 'WIS': 10, 'CHAR': 4, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  22 (4d8 + 4) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The shark has advantage on an attack roll against a creature if at least one of the shark's allies is within 5 feet of the creature and the ally isn't incapacitated.Water Breathing. The shark can brea"""
        return "The shark has advantage on an attack roll against a creature if at least one of the shark's allies is within 5 feet of the creature and the ally isn't incapacitated.Water Breathing. The shark can brea"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

