# bases1/venom-troll.py
"""
VenomTroll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=venom-troll
"""
from creature_base import GlobalCreatureBaseClass


class VenomTroll(GlobalCreatureBaseClass):
    """
    Large Giant creature - VenomTroll
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 94, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 20, 'INT': 7, 'WIS': 9, 'CHAR': 7, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  94 (9d10 + 45) Speed  30 ft. STR 18 (+4) DEX 13 (+1) CON 20 (+5) INT 7 (-2) WIS 9 (-1) CHA 7 (-2) Skills  Perception +2 Damage Immunities  poison Condition Immunities  poisoned Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

