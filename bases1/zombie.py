# bases1/zombie.py
"""
Zombie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zombie
"""
from creature_base import GlobalCreatureBaseClass


class Zombie(GlobalCreatureBaseClass):
    """
    Medium undead creature - Zombie
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 6, 'CON': 16, 'INT': 3, 'WIS': 6, 'CHAR': 5, 'armor_class': 8, 'alignment': 'neutral evil Armor Class  8 Hit Points  22 (3d8 + 9) Speed  20 ft. STR 13 (+1) DEX 6 (-2) CON 16 (+3) INT 3 (-4) WIS 6 (-2) CHA 5 (-3) Saving Throws  Wis +0 Damage Immunities  poison Condition Immunities  poisoned Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['undead_fortitude', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def undead_fortitude(self) -> str:
        """If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie """
        return 'If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie '

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage.'

