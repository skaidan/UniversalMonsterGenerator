# bases1/mummified-warrior.py
"""
MummifiedWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mummified-warrior
"""
from creature_base import GlobalCreatureBaseClass


class MummifiedWarrior(GlobalCreatureBaseClass):
    """
    Medium undead creature - MummifiedWarrior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 6, 'CON': 14, 'INT': 8, 'WIS': 6, 'CHAR': 8, 'armor_class': 8, 'alignment': 'neutral Armor Class  8 Hit Points  19 (3d8 + 6) Speed  20 ft. STR 13 (+1) DEX 6 (-2) CON 14 (+2) INT 8 (-1) WIS 6 (-2) CHA 8 (-1) Saving Throws  Wis +0 Damage Immunities  poison Condition Immunities  poisoned Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['undead_fortitude', 'spear']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def undead_fortitude(self) -> str:
        """If damage reduces the mummified warrior to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, """
        return 'If damage reduces the mummified warrior to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, '

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.'

