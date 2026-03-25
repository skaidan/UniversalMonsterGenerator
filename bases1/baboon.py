# bases1/baboon.py
"""
Baboon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=baboon
"""
from creature_base import GlobalCreatureBaseClass


class Baboon(GlobalCreatureBaseClass):
    """
    Small beast creature - Baboon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 3, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 14, 'CON': 11, 'INT': 4, 'WIS': 12, 'CHAR': 6, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  3 (1d6) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The baboon has advantage on an attack roll against a creature if at least one of the baboon's allies is within 5 feet of the creature and the ally isn't incapacitated."""
        return "The baboon has advantage on an attack roll against a creature if at least one of the baboon's allies is within 5 feet of the creature and the ally isn't incapacitated."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) piercing damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) piercing damage.'

