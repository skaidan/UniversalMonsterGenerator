# bases1/choker.py
"""
Choker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=choker
"""
from creature_base import GlobalCreatureBaseClass


class Choker(GlobalCreatureBaseClass):
    """
    Choker creature
    Size: Large, Type: or smaller creature, it is grappled (escape DC 15). Until this grapple ends, the target is restrained, and the choker can't use this tentacle on another target. The choker has two tentacles. If this attack is a critical hit, the target also can't breathe or speak until the grapple ends.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller creature, it is grappled (escape DC 15). Until this grapple ends, the target is restrained, and the choker can't use this tentacle on another target. The choker has two tentacles. If this attack is a critical hit, the target also can't breathe or speak until the grapple ends.",
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
        # Add creature-specific abilities
        self.abilities.extend(['aberrant_quickness_recharges_after_a_short_or_long_rest'])

    def aberrant_quickness_recharges_after_a_short_or_long_rest(self) -> str:
        """Aberrant Quickness (Recharges after a Short or Long Rest): The choker can take an extra action on its turn.Boneless. The choker can move through and occupy a s..."""
        return "The choker can take an extra action on its turn.Boneless. The choker can move through and occupy a space as narrow as 4 inches wide without squeezing.Spider Climb. The choker can climb difficult surfa"

