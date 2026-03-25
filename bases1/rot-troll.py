# bases1/rot-troll.py
"""
RotTroll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rot-troll
"""
from creature_base import GlobalCreatureBaseClass


class RotTroll(GlobalCreatureBaseClass):
    """
    Large Giant creature - RotTroll
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 138, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 22, 'INT': 5, 'WIS': 8, 'CHAR': 4, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  138 (12d10 + 72) Speed  30 ft. STR 18 (+4) DEX 13 (+1) CON 22 (+6) INT 5 (-3) WIS 8 (-1) CHA 4 (-3) Skills  Perception +3 Damage Immunities  necrotic Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

