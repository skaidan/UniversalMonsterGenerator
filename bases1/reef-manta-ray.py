# bases1/reef-manta-ray.py
"""
ReefMantaRay creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=reef-manta-ray
"""
from creature_base import GlobalCreatureBaseClass


class ReefMantaRay(GlobalCreatureBaseClass):
    """
    Large beast creature - ReefMantaRay
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 16, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 12, 'CON': 12, 'INT': 1, 'WIS': 12, 'CHAR': 4, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  16 (3d8 + 3) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'ram']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the manta ray moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature,"""
        return 'If the manta ray moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature,'

    def ram_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage.'

