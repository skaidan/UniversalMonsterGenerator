# bases1/acererak.py
"""
Acererak creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=acererak
"""
from creature_base import GlobalCreatureBaseClass


class Acererak(GlobalCreatureBaseClass):
    """
    Medium undead creature - Acererak
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 285, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 16, 'CON': 20, 'INT': 27, 'WIS': 21, 'CHAR': 20, 'armor_class': 21, 'alignment': 'neutral evil Armor Class  21 (natural armor) Hit Points  285 (30d8 + 150) Speed  30 ft. STR 13 (+1) DEX 16 (+3) CON 20 (+5) INT 27 (+8) WIS 21 (+5) CHA 20 (+5) Saving Throws  Con +12', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

