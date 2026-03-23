# bases1/giff.py
"""
Giff creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giff
"""
from creature_base import GlobalCreatureBaseClass


class Giff(GlobalCreatureBaseClass):
    """
    Giff creature
    Size: Large, Type: or smaller creature, that creature must succeed on a DC 14 Strength saving throw or take 7 (2d6) bludgeoning damage and be knocked prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 60,
        "min_level": 4,
        "level": 4,
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
        "type": "or smaller creature, that creature must succeed on a DC 14 Strength saving throw or take 7 (2d6) bludgeoning damage and be knocked prone.",
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
        # Add creature-specific abilities
        self.abilities.extend(['firearms_knowledge'])

    def firearms_knowledge(self) -> str:
        """Firearms Knowledge: The giff's mastery of its weapons enables it to ignore the loading property of muskets and pistols.H..."""
        return "The giff's mastery of its weapons enables it to ignore the loading property of muskets and pistols.Headfirst Charge. The giff can try to knock a creature over; if the giff moves at least 20 feet in a "

