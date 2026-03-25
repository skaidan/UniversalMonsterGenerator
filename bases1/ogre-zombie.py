# bases1/ogre-zombie.py
"""
OgreZombie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ogre-zombie
"""
from creature_base import GlobalCreatureBaseClass


class OgreZombie(GlobalCreatureBaseClass):
    """
    Large undead creature - OgreZombie
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 6, 'CON': 18, 'INT': 3, 'WIS': 6, 'CHAR': 5, 'armor_class': 8, 'alignment': 'neutral evil Armor Class  8 Hit Points  85 (9d10 + 36) Speed  30 ft. STR 19 (+4) DEX 6 (-2) CON 18 (+4) INT 3 (-4) WIS 6 (-2) CHA 5 (-3) Saving Throws  Wis +0 Damage Immunities  poison Condition Immunities  poisoned Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['undead_fortitude', 'morningstar']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def undead_fortitude(self) -> str:
        """If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie """
        return 'If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie '

    def morningstar_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.'

