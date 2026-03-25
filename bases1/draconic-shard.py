# bases1/draconic-shard.py
"""
DraconicShard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconic-shard
"""
from creature_base import GlobalCreatureBaseClass


class DraconicShard(GlobalCreatureBaseClass):
    """
    Huge Undead creature - DraconicShard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 168, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 12, 'CON': 18, 'INT': 22, 'WIS': 18, 'CHAR': 22, 'armor_class': 17, 'alignment': 'typically Neutral Armor Class  17 (Deflection) Hit Points  168 (16d12 + 64) Speed  0 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

