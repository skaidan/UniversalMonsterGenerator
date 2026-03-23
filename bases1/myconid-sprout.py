# bases1/myconid-sprout.py
"""
MyconidSprout creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=myconid-sprout
"""
from creature_base import GlobalCreatureBaseClass


class MyconidSprout(GlobalCreatureBaseClass):
    """
    MyconidSprout creature
    Size: Small, Type: plant, lawful neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 7,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "plant, lawful neutral",
        "hit_points_up": [1, 1, 1],
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
        self.abilities.extend(['distress_spores'])

    def distress_spores(self) -> str:
        """Distress Spores: When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickn..."""
        return "When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr"
    def distress_spores(self) -> str:
        """Distress Spores: When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickn..."""
        return "When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr"

