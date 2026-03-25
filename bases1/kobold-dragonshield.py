# bases1/kobold-dragonshield.py
"""
KoboldDragonshield creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kobold-dragonshield
"""
from creature_base import GlobalCreatureBaseClass


class KoboldDragonshield(GlobalCreatureBaseClass):
    """
    Small Dragon creature - KoboldDragonshield
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 44, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 15, 'CON': 14, 'INT': 8, 'WIS': 9, 'CHAR': 10, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (leather', 'legendary': False, 'size': 'Small', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['dragons_resistance', 'multiattack', 'spear']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dragons_resistance(self) -> str:
        """The kobold has resistance to a type of damage based on the color of dragon that invested it with power (choose or roll a d10): 1–2, acid (black or copper); 3–4, cold (silver or white); 5–6, fire (bras"""
        return 'The kobold has resistance to a type of damage based on the color of dragon that invested it with power (choose or roll a d10): 1–2, acid (black or copper); 3–4, cold (silver or white); 5–6, fire (bras'

    def multiattack_attack(self) -> str:
        """The kobold makes two Spear attacks."""
        return 'The kobold makes two Spear attacks.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.'

