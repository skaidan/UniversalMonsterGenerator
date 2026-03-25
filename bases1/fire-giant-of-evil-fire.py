# bases1/fire-giant-of-evil-fire.py
"""
FireGiantOfEvilFire creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-giant-of-evil-fire
"""
from creature_base import GlobalCreatureBaseClass


class FireGiantOfEvilFire(GlobalCreatureBaseClass):
    """
    Huge Giant creature - FireGiantOfEvilFire
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 150, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 9, 'CON': 23, 'INT': 10, 'WIS': 19, 'CHAR': 14, 'armor_class': 18, 'alignment': 'typically Lawful Evil Armor Class  18 (plate) Hit Points  150 (12d12 + 72) Speed  30 ft. STR 25 (+7) DEX 9 (-1) CON 23 (+6) INT 10 (+0) WIS 19 (+4) CHA 14 (+2) Saving Throws  Con +10', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

