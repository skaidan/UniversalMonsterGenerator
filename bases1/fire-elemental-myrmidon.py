# bases1/fire-elemental-myrmidon.py
"""
FireElementalMyrmidon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-elemental-myrmidon
"""
from creature_base import GlobalCreatureBaseClass


class FireElementalMyrmidon(GlobalCreatureBaseClass):
    """
    Medium Elemental creature - FireElementalMyrmidon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 18, 'CON': 15, 'INT': 9, 'WIS': 10, 'CHAR': 10, 'armor_class': 18, 'alignment': 'typically Neutral Armor Class  18 (plate) Hit Points  123 (19d8 + 38) Speed  40 ft. STR 13 (+1) DEX 18 (+4) CON 15 (+2) INT 9 (-1) WIS 10 (+0) CHA 10 (+0) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

