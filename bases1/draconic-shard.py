# bases1/draconic-shard.py
"""
DraconicShard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconic-shard
"""
from creature_base import GlobalCreatureBaseClass


class DraconicShard(GlobalCreatureBaseClass):
    """
    DraconicShard creature
    Size: Huge, Type: Undead, typically Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 168,
        "min_level": 18,
        "level": 18,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Undead, typically Neutral",
        "hit_points_up": [16, 16, 16],
        "STR_up": [1, 0, 0],
        "DEX_up": [1, 0, 0],
        "CON_up": [0, 1, 0],
        "INT_up": [0, 1, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 1],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Add creature-specific abilities
        # No special abilities

