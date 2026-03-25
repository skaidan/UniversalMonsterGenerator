# bases1/swashbuckler.py
"""
Swashbuckler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swashbuckler
"""
from creature_base import GlobalCreatureBaseClass


class Swashbuckler(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - Swashbuckler
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 18, 'CON': 12, 'INT': 14, 'WIS': 11, 'CHAR': 15, 'armor_class': 17, 'alignment': 'any alignment Armor Class  17 (leather armor', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['suave_defense', 'multiattack', 'dagger', 'rapier']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def suave_defense(self) -> str:
        """While the swashbuckler is wearing light or no armor and wielding no shield, its AC includes its Charisma modifier."""
        return 'While the swashbuckler is wearing light or no armor and wielding no shield, its AC includes its Charisma modifier.'

    def multiattack_attack(self) -> str:
        """The swashbuckler makes one Dagger attack and two Rapier attacks."""
        return 'The swashbuckler makes one Dagger attack and two Rapier attacks.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 6 (1d4 + 4) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 6 (1d4 + 4) piercing damage.'

    def rapier_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.'

