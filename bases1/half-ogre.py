# bases1/half-ogre.py
"""
HalfOgre creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=half-ogre
"""
from creature_base import GlobalCreatureBaseClass


class HalfOgre(GlobalCreatureBaseClass):
    """
    Large giant creature - HalfOgre
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 30, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 14, 'INT': 7, 'WIS': 9, 'CHAR': 10, 'armor_class': 12, 'alignment': 'any chaotic alignment Armor Class  12 (hide armor) Hit Points  30 (4d10 + 8) Speed  30 ft. STR 17 (+3) DEX 10 (+0) CON 14 (+2) INT 7 (-2) WIS 9 (-1) CHA 10 (+0) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['battleaxe', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def battleaxe_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2d10 + 3) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2d10 + 3) slashing damage if used with two hands.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 10 (2d6 + 3) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 10 (2d6 + 3) piercing damage.'

