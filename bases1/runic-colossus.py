# bases1/runic-colossus.py
"""
RunicColossus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=runic-colossus
"""
from creature_base import GlobalCreatureBaseClass


class RunicColossus(GlobalCreatureBaseClass):
    """
    Gargantuan Construct creature - RunicColossus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 315, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 9, 'CON': 24, 'INT': 3, 'WIS': 11, 'CHAR': 1, 'armor_class': 20, 'alignment': 'unaligned Armor Class  20 (natural armor) Hit Points  315 (18d20 + 126) Speed  60 ft. STR 25 (+7) DEX 9 (-1) CON 24 (+7) INT 3 (-4) WIS 11 (+0) CHA 1 (-5) Damage Resistances  acid', 'legendary': False, 'size': 'Gargantuan', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

