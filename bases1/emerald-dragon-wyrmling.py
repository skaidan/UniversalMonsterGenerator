# bases1/emerald-dragon-wyrmling.py
"""
EmeraldDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=emerald-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class EmeraldDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Gem) creature - EmeraldDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 12, 'CON': 15, 'INT': 14, 'WIS': 12, 'CHAR': 14, 'armor_class': 16, 'alignment': 'typically Lawful Neutral Armor Class  16 (natural armor) Hit Points  39 (6d8 + 12) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

