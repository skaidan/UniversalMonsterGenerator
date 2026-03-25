# bases1/winged-kobold.py
"""
WingedKobold creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=winged-kobold
"""
from creature_base import GlobalCreatureBaseClass


class WingedKobold(GlobalCreatureBaseClass):
    """
    Small humanoid (Kobold) creature - WingedKobold
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 16, 'CON': 9, 'INT': 8, 'WIS': 7, 'CHAR': 8, 'armor_class': 13, 'alignment': 'lawful evil Armor Class  13 Hit Points  7 (3d6 - 3) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'humanoid (Kobold)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['sunlight_sensitivity', 'dagger', 'dropped_rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sunlight_sensitivity(self) -> str:
        """While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.Pack Tactics. The kobold has advantage on an attack roll against a creature """
        return 'While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.Pack Tactics. The kobold has advantage on an attack roll against a creature '

    def dagger_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.'

    def dropped_rock_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, one target directly below the kobold. Hit: 6 (1d6 + 3) bludgeoning damage."""
        return 'Ranged Weapon Attack: +5 to hit, one target directly below the kobold. Hit: 6 (1d6 + 3) bludgeoning damage.'

