# bases1/cadaver-collector.py
"""
CadaverCollector creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cadaver-collector
"""
from creature_base import GlobalCreatureBaseClass


class CadaverCollector(GlobalCreatureBaseClass):
    """
    Large Construct creature - CadaverCollector
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 14, 'CON': 20, 'INT': 5, 'WIS': 11, 'CHAR': 8, 'armor_class': 17, 'alignment': 'typically Lawful Evil Armor Class  17 (natural armor) Hit Points  189 (18d10 + 90) Speed  30 ft. STR 21 (+5) DEX 14 (+2) CON 20 (+5) INT 5 (-3) WIS 11 (+0) CHA 8 (-1) Damage Immunities  necrotic', 'legendary': False, 'size': 'Large', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

