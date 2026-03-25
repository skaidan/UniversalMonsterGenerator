# bases1/baphomet.py
"""
Baphomet creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=baphomet
"""
from creature_base import GlobalCreatureBaseClass


class Baphomet(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - Baphomet
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 319, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 14, 'CON': 26, 'INT': 18, 'WIS': 24, 'CHAR': 16, 'armor_class': 22, 'alignment': 'Chaotic Evil Armor Class  22 (natural armor) Hit Points  319 (22d12 + 176) Speed  40 ft. STR 30 (+10) DEX 14 (+2) CON 26 (+8) INT 18 (+4) WIS 24 (+7) CHA 16 (+3) Saving Throws  Dex +9', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

