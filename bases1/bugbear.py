# bases1/bugbear.py
"""
Bugbear creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bugbear
"""
from creature_base import GlobalCreatureBaseClass


class Bugbear(GlobalCreatureBaseClass):
    """
    Medium humanoid (Goblinoid) creature - Bugbear
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 13, 'INT': 8, 'WIS': 11, 'CHAR': 9, 'armor_class': 16, 'alignment': 'chaotic evil Armor Class  16 (hide armor', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['brute', 'morningstar', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def brute(self) -> str:
        """A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the attack).Surprise Attack. If the bugbear surprises a creature and hits it with an attack during the first"""
        return 'A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the attack).Surprise Attack. If the bugbear surprises a creature and hits it with an attack during the first'

    def morningstar_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 11 (2d8 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 11 (2d8 + 2) piercing damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 9 (2d6 + 2) piercing damage in melee or 5 (1d6 + 2) piercing damage at range."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 9 (2d6 + 2) piercing damage in melee or 5 (1d6 + 2) piercing damage at range.'

