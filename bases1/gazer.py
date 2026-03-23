# bases1/gazer.py
"""
Gazer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gazer
"""
from creature_base import GlobalCreatureBaseClass


class Gazer(GlobalCreatureBaseClass):
    """
    Gazer creature
    Size: Medium, Type: or smaller, it must succeed on a DC 12 Strength saving throw or be moved up to 30 feet directly away from the gazer. If the target is a Tiny object that isn't being worn or carried, the gazer moves it up to 30 feet in any direction. The gazer can also exert fine control on objects with this ray, such as manipulating a simple tool or opening a container.
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
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, it must succeed on a DC 12 Strength saving throw or be moved up to 30 feet directly away from the gazer. If the target is a Tiny object that isn't being worn or carried, the gazer moves it up to 30 feet in any direction. The gazer can also exert fine control on objects with this ray, such as manipulating a simple tool or opening a container.",
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
        self.abilities.extend(['mimicry'])

    def mimicry(self) -> str:
        """Mimicry: The gazer can mimic simple sounds of speech it has heard, in any language. A creature that hears the..."""
        return "The gazer can mimic simple sounds of speech it has heard, in any language. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check.ActionsBite. Mel"

