# bases1/stalker-of-baphomet.py
"""
StalkerOfBaphomet creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stalker-of-baphomet
"""
from creature_base import GlobalCreatureBaseClass


class StalkerOfBaphomet(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - StalkerOfBaphomet
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 200, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 17, 'CON': 22, 'INT': 13, 'WIS': 16, 'CHAR': 12, 'armor_class': 17, 'alignment': 'typically Chaotic Evil Armor Class  17 (natural armor) Hit Points  200 (16d12 + 96) Speed  40 ft. STR 25 (+7) DEX 17 (+3) CON 22 (+6) INT 13 (+1) WIS 16 (+3) CHA 12 (+1) Saving Throws  Dex +7', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

