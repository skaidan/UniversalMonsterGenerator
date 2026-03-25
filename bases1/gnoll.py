# bases1/gnoll.py
"""
Gnoll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll
"""
from creature_base import GlobalCreatureBaseClass


class Gnoll(GlobalCreatureBaseClass):
    """
    Medium humanoid (Gnoll) creature - Gnoll
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 12, 'CON': 11, 'INT': 6, 'WIS': 10, 'CHAR': 7, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (hide armor', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Gnoll)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['rampage', 'bite', 'spear', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def rampage(self) -> str:
        """When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."""
        return 'When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target. Hit: 5 (1d8 + 1) piercing damage."""
        return 'Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target. Hit: 5 (1d8 + 1) piercing damage.'

