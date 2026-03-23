# bases1/glabrezu.py
"""
Glabrezu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=glabrezu
"""
from creature_base import GlobalCreatureBaseClass


class Glabrezu(GlobalCreatureBaseClass):
    """
    Glabrezu creature
    Size: Medium, Type: or smaller creature, it is grappled (escape DC 15). The glabrezu has two pincers, each of which can grapple only one target.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 157,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature, it is grappled (escape DC 15). The glabrezu has two pincers, each of which can grapple only one target.",
        "hit_points_up": [15, 15, 15],
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
        self.abilities.extend(['innate_spellcasting'])

    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The glabrezu's spellcasting ability is Intelligence (spell save DC 16). The glabrezu can innately ca..."""
        return "The glabrezu's spellcasting ability is Intelligence (spell save DC 16). The glabrezu can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel ma"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The glabrezu's spellcasting ability is Intelligence (spell save DC 16). The glabrezu can innately ca..."""
        return "The glabrezu's spellcasting ability is Intelligence (spell save DC 16). The glabrezu can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel ma"

