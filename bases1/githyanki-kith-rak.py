# bases1/githyanki-kith-rak.py
"""
GithyankiKithRak creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githyanki-kith-rak
"""
from creature_base import GlobalCreatureBaseClass


class GithyankiKithRak(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Gith) creature - GithyankiKithRak
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 180, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 16, 'CON': 17, 'INT': 16, 'WIS': 15, 'CHAR': 17, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  180 (24d8 + 72) Speed  30 ft. STR 18 (+4) DEX 16 (+3) CON 17 (+3) INT 16 (+3) WIS 15 (+2) CHA 17 (+3) Saving Throws  Con +7', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

