# bases1/leucrotta.py
"""
Leucrotta creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=leucrotta
"""
from creature_base import GlobalCreatureBaseClass


class Leucrotta(GlobalCreatureBaseClass):
    """
    Leucrotta creature
    Size: Large, Type: Monstrosity, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 67,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Monstrosity, typically Chaotic Evil",
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
        self.abilities.extend(['mimicry'])

    def mimicry(self) -> str:
        """Mimicry: The leucrotta can mimic Beast sounds and Humanoid voices. A creature that hears the sounds can tell ..."""
        return "The leucrotta can mimic Beast sounds and Humanoid voices. A creature that hears the sounds can tell they are imitations only with a successful DC 14 Wisdom (Insight) check.Stench. Any creature other t"

