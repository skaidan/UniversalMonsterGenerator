# bases1/myconid-sovereign.py
"""
MyconidSovereign creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=myconid-sovereign
"""
from creature_base import GlobalCreatureBaseClass


class MyconidSovereign(GlobalCreatureBaseClass):
    """
    MyconidSovereign creature
    Size: Large, Type: or smaller beast within 5 feet of it and releases spores at the corpse. In 24 hours, the corpse rises as a spore servant. The corpse stays animated for 1d4 + 1 weeks or until destroyed, and it can't be animated again in this way.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 60,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller beast within 5 feet of it and releases spores at the corpse. In 24 hours, the corpse rises as a spore servant. The corpse stays animated for 1d4 + 1 weeks or until destroyed, and it can't be animated again in this way.",
        "hit_points_up": [6, 6, 6],
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

