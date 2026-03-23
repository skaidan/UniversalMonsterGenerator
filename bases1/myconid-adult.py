# bases1/myconid-adult.py
"""
MyconidAdult creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=myconid-adult
"""
from creature_base import GlobalCreatureBaseClass


class MyconidAdult(GlobalCreatureBaseClass):
    """
    MyconidAdult creature
    Size: Medium, Type: plant, lawful neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "plant, lawful neutral",
        "hit_points_up": [2, 2, 2],
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

