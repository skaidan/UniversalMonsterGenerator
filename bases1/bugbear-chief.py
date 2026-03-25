# bases1/bugbear-chief.py
"""
BugbearChief creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bugbear-chief
"""
from creature_base import GlobalCreatureBaseClass


class BugbearChief(GlobalCreatureBaseClass):
    """
    Medium humanoid (Goblinoid) creature - BugbearChief
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 65, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 14, 'CON': 14, 'INT': 11, 'WIS': 12, 'CHAR': 11, 'armor_class': 17, 'alignment': 'chaotic evil Armor Class  17 (chain shirt', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['brute', 'multiattack', 'morningstar', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def brute(self) -> str:
        """A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the attack).Heart of Hruggek. The bugbear has advantage on saving throws against being charmed, frightened, """
        return 'A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the attack).Heart of Hruggek. The bugbear has advantage on saving throws against being charmed, frightened, '

    def multiattack_attack(self) -> str:
        """The bugbear makes two melee attacks."""
        return 'The bugbear makes two melee attacks.'

    def morningstar_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 10 (2d6 + 3) piercing damage in melee or 6 (1d6 + 3) piercing damage at range."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 10 (2d6 + 3) piercing damage in melee or 6 (1d6 + 3) piercing damage at range.'

