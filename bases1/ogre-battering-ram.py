# bases1/ogre-battering-ram.py
"""
OgreBatteringRam creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ogre-battering-ram
"""
from creature_base import GlobalCreatureBaseClass


class OgreBatteringRam(GlobalCreatureBaseClass):
    """
    Large Giant creature - OgreBatteringRam
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 76, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 8, 'CON': 16, 'INT': 5, 'WIS': 7, 'CHAR': 7, 'armor_class': 11, 'alignment': 'typically Chaotic Evil Armor Class  11 (hide armor) Hit Points  76 (9d10 + 27) Speed  40 ft. STR 19 (+4) DEX 8 (-1) CON 16 (+3) INT 5 (-3) WIS 7 (-2) CHA 7 (-2) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

