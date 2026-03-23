# bases1/skulk.py
"""
Skulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=skulk
"""
from creature_base import GlobalCreatureBaseClass


class Skulk(GlobalCreatureBaseClass):
    """
    Skulk creature
    Size: Medium, Type: Monstrosity, typically Chaotic Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 18,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Monstrosity, typically Chaotic Neutral",
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
        self.abilities.extend(['fallible_invisibility'])

    def fallible_invisibility(self) -> str:
        """Fallible Invisibility: The skulk is invisible. This invisibility can be circumvented by three things:Charnel Candles. The s..."""
        return "The skulk is invisible. This invisibility can be circumvented by three things:Charnel Candles. The skulk appears as a dim, translucent form in the light of a candle made of fat rendered from a corpse "

