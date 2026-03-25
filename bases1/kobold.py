# bases1/kobold.py
"""
Kobold creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kobold
"""
from creature_base import GlobalCreatureBaseClass


class Kobold(GlobalCreatureBaseClass):
    """
    Small humanoid (Kobold) creature - Kobold
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 5, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 15, 'CON': 9, 'INT': 8, 'WIS': 7, 'CHAR': 8, 'armor_class': 12, 'alignment': 'lawful evil Armor Class  12 Hit Points  5 (2d6 - 2) Speed  30 ft. STR 7 (-2) DEX 15 (+2) CON 9 (-1) INT 8 (-1) WIS 7 (-2) CHA 8 (-1) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'humanoid (Kobold)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['sunlight_sensitivity', 'dagger', 'sling']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sunlight_sensitivity(self) -> str:
        """While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.Pack Tactics. The kobold has advantage on an attack roll against a creature """
        return 'While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.Pack Tactics. The kobold has advantage on an attack roll against a creature '

    def dagger_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def sling_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.'

