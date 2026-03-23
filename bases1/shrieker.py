# bases1/shrieker.py
"""
Shrieker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shrieker
"""
from creature_base import GlobalCreatureBaseClass


class Shrieker(GlobalCreatureBaseClass):
    """
    Shrieker creature
    Size: Medium, Type: plant, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 5,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "plant, unaligned",
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the shrieker remains motionless, it is indistinguishable from an ordinary fungus.ReactionsShri..."""
        return "While the shrieker remains motionless, it is indistinguishable from an ordinary fungus.ReactionsShriek. When bright light or a creature is within 30 feet of the shrieker, it emits a shriek audible wit"
    def false_appearance(self) -> str:
        """False Appearance: While the shrieker remains motionless, it is indistinguishable from an ordinary fungus.ReactionsShri..."""
        return "While the shrieker remains motionless, it is indistinguishable from an ordinary fungus.ReactionsShriek. When bright light or a creature is within 30 feet of the shrieker, it emits a shriek audible wit"

