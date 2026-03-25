# bases1/invisible-stalker.py
"""
InvisibleStalker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=invisible-stalker
"""
from creature_base import GlobalCreatureBaseClass


class InvisibleStalker(GlobalCreatureBaseClass):
    """
    Medium elemental creature - InvisibleStalker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 104, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 19, 'CON': 14, 'INT': 10, 'WIS': 15, 'CHAR': 11, 'armor_class': 14, 'alignment': 'neutral Armor Class  14 Hit Points  104 (16d8 + 32) Speed  50 ft.', 'legendary': False, 'size': 'Medium', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['invisibility', 'multiattack', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def invisibility(self) -> str:
        """The stalker is invisible.Faultless Tracker. The stalker is given a quarry by its summoner. The stalker knows the direction and distance to its quarry as long as the two of them are on the same plane o"""
        return 'The stalker is invisible.Faultless Tracker. The stalker is given a quarry by its summoner. The stalker knows the direction and distance to its quarry as long as the two of them are on the same plane o'

    def multiattack_attack(self) -> str:
        """The stalker makes two slam attacks."""
        return 'The stalker makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage.'

