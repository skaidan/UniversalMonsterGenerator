# bases1/shrieker.py
"""
Shrieker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shrieker
"""
from creature_base import GlobalCreatureBaseClass


class Shrieker(GlobalCreatureBaseClass):
    """
    Medium plant creature - Shrieker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 1, 'CON': 10, 'INT': 1, 'WIS': 3, 'CHAR': 1, 'armor_class': 5, 'alignment': 'unaligned Armor Class  5 Hit Points  13 (3d8) Speed  0 ft. STR 1 (-5) DEX 1 (-5) CON 10 (+0) INT 1 (-5) WIS 3 (-4) CHA 1 (-5) Condition Immunities  blinded', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the shrieker remains motionless, it is indistinguishable from an ordinary fungus.ReactionsShriek. When bright light or a creature is within 30 feet of the shrieker, it emits a shriek audible wit"""
        return 'While the shrieker remains motionless, it is indistinguishable from an ordinary fungus.ReactionsShriek. When bright light or a creature is within 30 feet of the shrieker, it emits a shriek audible wit'

