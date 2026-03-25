# bases1/ogre.py
"""
Ogre creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ogre
"""
from creature_base import GlobalCreatureBaseClass


class Ogre(GlobalCreatureBaseClass):
    """
    Large giant creature - Ogre
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 59, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 8, 'CON': 16, 'INT': 5, 'WIS': 7, 'CHAR': 7, 'armor_class': 11, 'alignment': 'chaotic evil Armor Class  11 (hide armor) Hit Points  59 (7d10 + 21) Speed  40 ft. STR 19 (+4) DEX 8 (-1) CON 16 (+3) INT 5 (-3) WIS 7 (-2) CHA 7 (-2) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['greatclub', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def greatclub_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 11 (2d6 + 4) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 11 (2d6 + 4) piercing damage.'

