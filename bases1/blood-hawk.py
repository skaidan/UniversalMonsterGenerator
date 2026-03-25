# bases1/blood-hawk.py
"""
BloodHawk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blood-hawk
"""
from creature_base import GlobalCreatureBaseClass


class BloodHawk(GlobalCreatureBaseClass):
    """
    Small beast creature - BloodHawk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 14, 'CON': 10, 'INT': 3, 'WIS': 14, 'CHAR': 5, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  7 (2d6) Speed  10 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'beak']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The hawk has advantage on Wisdom (Perception) checks that rely on sight.Pack Tactics. The hawk has advantage on an attack roll against a creature if at least one of the hawk's allies is within 5 feet """
        return "The hawk has advantage on Wisdom (Perception) checks that rely on sight.Pack Tactics. The hawk has advantage on an attack roll against a creature if at least one of the hawk's allies is within 5 feet "

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

