# bases1/abominable-yeti.py
"""
AbominableYeti creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=abominable-yeti
"""
from creature_base import GlobalCreatureBaseClass


class AbominableYeti(GlobalCreatureBaseClass):
    """
    AbominableYeti creature
    Size: Huge, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 137,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "monstrosity, chaotic evil",
        "hit_points_up": [13, 13, 13],
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
        self.abilities.extend(['fear_of_fire'])

    def fear_of_fire(self) -> str:
        """Fear of Fire: If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end ..."""
        return "If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.Keen Smell. The yeti has advantage on Wisdom (Perception) checks that rely on smell"
    def fear_of_fire(self) -> str:
        """Fear of Fire: If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end ..."""
        return "If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.Keen Smell. The yeti has advantage on Wisdom (Perception) checks that rely on smell"

