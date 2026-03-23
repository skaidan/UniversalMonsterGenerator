# bases1/gem-greatwyrm.py
"""
GemGreatwyrm creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gem-greatwyrm
"""
from creature_base import GlobalCreatureBaseClass


class GemGreatwyrm(GlobalCreatureBaseClass):
    """
    GemGreatwyrm creature
    Size: Gargantuan, Type: Dragon (Gem), typically Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 507,
        "min_level": 27,
        "level": 27,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 21,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Dragon (Gem), typically Neutral",
        "hit_points_up": [50, 50, 50],
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

