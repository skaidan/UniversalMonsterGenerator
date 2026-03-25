# bases1/gnoll-flesh-gnawer.py
"""
GnollFleshGnawer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll-flesh-gnawer
"""
from creature_base import GlobalCreatureBaseClass


class GnollFleshGnawer(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - GnollFleshGnawer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 14, 'CON': 12, 'INT': 8, 'WIS': 10, 'CHAR': 8, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (studded leather) Hit Points  22 (4d8 + 4) Speed  30 ft. STR 12 (+1) DEX 14 (+2) CON 12 (+1) INT 8 (-1) WIS 10 (+0) CHA 8 (-1) Saving Throws  Dex +4 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

