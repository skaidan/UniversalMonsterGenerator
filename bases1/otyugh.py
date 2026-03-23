# bases1/otyugh.py
"""
Otyugh creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=otyugh
"""
from creature_base import GlobalCreatureBaseClass


class Otyugh(GlobalCreatureBaseClass):
    """
    Otyugh creature
    Size: Medium, Type: or smaller, it is grappled (escape DC 13) and restrained until the grapple ends. The otyugh has two tentacles, each of which can grapple one target.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 114,
        "min_level": 6,
        "level": 6,
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
        "type": "or smaller, it is grappled (escape DC 13) and restrained until the grapple ends. The otyugh has two tentacles, each of which can grapple one target.",
        "hit_points_up": [11, 11, 11],
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
        self.abilities.extend(['limited_telepathy'])

    def limited_telepathy(self) -> str:
        """Limited Telepathy: The otyugh can magically transmit simple messages and images to any creature within 120 feet of it t..."""
        return "The otyugh can magically transmit simple messages and images to any creature within 120 feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepa"
    def limited_telepathy(self) -> str:
        """Limited Telepathy: The otyugh can magically transmit simple messages and images to any creature within 120 feet of it t..."""
        return "The otyugh can magically transmit simple messages and images to any creature within 120 feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepa"

