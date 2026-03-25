# bases1/sivak-draconian.py
"""
SivakDraconian creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sivak-draconian
"""
from creature_base import GlobalCreatureBaseClass


class SivakDraconian(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - SivakDraconian
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 57, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 18, 'INT': 13, 'WIS': 10, 'CHAR': 10, 'armor_class': 16, 'alignment': 'typically Lawful Evil Armor Class  16 (natural armor) Hit Points  57 (6d10 + 24) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

