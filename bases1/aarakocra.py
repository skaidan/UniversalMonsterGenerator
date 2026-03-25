# bases1/aarakocra.py
"""
Aarakocra creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=aarakocra
"""
from creature_base import GlobalCreatureBaseClass


class Aarakocra(GlobalCreatureBaseClass):
    """
    Medium humanoid (Aarakocra) creature - Aarakocra
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 10, 'INT': 11, 'WIS': 12, 'CHAR': 11, 'armor_class': 12, 'alignment': 'neutral good Armor Class  12 Hit Points  13 (3d8) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Aarakocra)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['dive_attack', 'talon', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dive_attack(self) -> str:
        """If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target."""
        return 'If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target.'

    def talon_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

