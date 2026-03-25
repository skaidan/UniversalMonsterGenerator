# bases1/strahd-von-zarovich.py
"""
StrahdVonZarovich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=strahd-von-zarovich
"""
from creature_base import GlobalCreatureBaseClass


class StrahdVonZarovich(GlobalCreatureBaseClass):
    """
    Medium undead (Shapechanger) creature - StrahdVonZarovich
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 144, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 18, 'CON': 18, 'INT': 20, 'WIS': 15, 'CHAR': 18, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (natural armor) Hit Points  144 (17d8 + 68) Speed  30 ft. STR 18 (+4) DEX 18 (+4) CON 18 (+4) INT 20 (+5) WIS 15 (+2) CHA 18 (+4) Saving Throws  Dex +9', 'legendary': False, 'size': 'Medium', 'type': 'undead (Shapechanger)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

