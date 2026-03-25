# bases1/bulezau.py
"""
Bulezau creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bulezau
"""
from creature_base import GlobalCreatureBaseClass


class Bulezau(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Bulezau
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 17, 'INT': 8, 'WIS': 9, 'CHAR': 6, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (natural armor) Hit Points  52 (7d8 + 21) Speed  40 ft. STR 15 (+2) DEX 14 (+2) CON 17 (+3) INT 8 (-1) WIS 9 (-1) CHA 6 (-2) Damage Resistances  cold', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

