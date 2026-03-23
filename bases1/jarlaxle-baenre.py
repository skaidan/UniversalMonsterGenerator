# bases1/jarlaxle-baenre.py
"""
JarlaxleBaenre creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=jarlaxle-baenre
"""
from creature_base import GlobalCreatureBaseClass


class JarlaxleBaenre(GlobalCreatureBaseClass):
    """
    JarlaxleBaenre creature
    Size: Medium, Type: humanoid (Elf), chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 123,
        "min_level": 16,
        "level": 16,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 3,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Elf), chaotic neutral",
        "hit_points_up": [12, 12, 12],
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

