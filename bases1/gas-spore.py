# bases1/gas-spore.py
"""
GasSpore creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gas-spore
"""
from creature_base import GlobalCreatureBaseClass


class GasSpore(GlobalCreatureBaseClass):
    """
    Large plant creature - GasSpore
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 5, 'DEX': 1, 'CON': 3, 'INT': 1, 'WIS': 1, 'CHAR': 1, 'armor_class': 5, 'alignment': 'unaligned Armor Class  5 Hit Points  1 (1d10 - 4) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_burst', 'touch']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_burst(self) -> str:
        """The gas spore explodes when it drops to 0 hit points. Each creature within 20 feet of it must succeed on a DC 15 Constitution saving throw or take 10 (3d6) poison damage and become infected with a dis"""
        return 'The gas spore explodes when it drops to 0 hit points. Each creature within 20 feet of it must succeed on a DC 15 Constitution saving throw or take 10 (3d6) poison damage and become infected with a dis'

    def touch_attack(self) -> str:
        """Melee Weapon Attack: +0 to hit, reach 5 ft., one creature. Hit: 1 poison damage, and the creature must succeed on a DC 10 Constitution saving throw or become infected with the disease described in the Death Burst trait."""
        return 'Melee Weapon Attack: +0 to hit, reach 5 ft., one creature. Hit: 1 poison damage, and the creature must succeed on a DC 10 Constitution saving throw or become infected with the disease described in the Death Burst trait.'

