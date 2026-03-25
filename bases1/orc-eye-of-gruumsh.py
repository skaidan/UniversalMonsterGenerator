# bases1/orc-eye-of-gruumsh.py
"""
OrcEyeOfGruumsh creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-eye-of-gruumsh
"""
from creature_base import GlobalCreatureBaseClass


class OrcEyeOfGruumsh(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - OrcEyeOfGruumsh
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 16, 'INT': 9, 'WIS': 13, 'CHAR': 12, 'armor_class': 16, 'alignment': 'chaotic evil Armor Class  16 (ring mail', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aggressive', 'spear']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aggressive(self) -> str:
        """As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruumsh's Fury. The orc deals an extra 4 (1d8) damage when it hits with a weapon attack (included in the a"""
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruumsh's Fury. The orc deals an extra 4 (1d8) damage when it hits with a weapon attack (included in the a"

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 11 (1d6 + 3 plus 1d8) piercing damage, or 12 (2d8 + 3) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 11 (1d6 + 3 plus 1d8) piercing damage, or 12 (2d8 + 3) piercing damage if used with two hands to make a melee attack.'

