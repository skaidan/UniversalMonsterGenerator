# bases1/quaggoth.py
"""
Quaggoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quaggoth
"""
from creature_base import GlobalCreatureBaseClass


class Quaggoth(GlobalCreatureBaseClass):
    """
    Medium humanoid (Quaggoth) creature - Quaggoth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 16, 'INT': 6, 'WIS': 12, 'CHAR': 7, 'armor_class': 13, 'alignment': 'chaotic neutral Armor Class  13 (natural armor) Hit Points  45 (6d8 + 18) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Quaggoth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['wounded_fury', 'multiattack', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def wounded_fury(self) -> str:
        """While it has 10 hit points or fewer, the quaggoth has advantage on attack rolls. In addition, it deals an extra 7 (2d6) damage to any target it hits with a melee attack."""
        return 'While it has 10 hit points or fewer, the quaggoth has advantage on attack rolls. In addition, it deals an extra 7 (2d6) damage to any target it hits with a melee attack.'

    def multiattack_attack(self) -> str:
        """The quaggoth makes two claw attacks."""
        return 'The quaggoth makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

