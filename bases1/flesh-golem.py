# bases1/flesh-golem.py
"""
FleshGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flesh-golem
"""
from creature_base import GlobalCreatureBaseClass


class FleshGolem(GlobalCreatureBaseClass):
    """
    Medium construct creature - FleshGolem
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 9, 'CON': 18, 'INT': 6, 'WIS': 10, 'CHAR': 5, 'armor_class': 9, 'alignment': 'neutral Armor Class  9 Hit Points  93 (11d8 + 44) Speed  30 ft. STR 19 (+4) DEX 9 (-1) CON 18 (+4) INT 6 (-2) WIS 10 (+0) CHA 5 (-3) Damage Immunities  lightning', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['berserk', 'multiattack', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def berserk(self) -> str:
        """Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no """
        return 'Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no '

    def multiattack_attack(self) -> str:
        """The golem makes two slam attacks."""
        return 'The golem makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.'

