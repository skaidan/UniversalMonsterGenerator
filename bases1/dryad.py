# bases1/dryad.py
"""
Dryad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dryad
"""
from creature_base import GlobalCreatureBaseClass


class Dryad(GlobalCreatureBaseClass):
    """
    Dryad creature
    Size: Large, Type: or bigger.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or bigger.",
        "hit_points_up": [2, 2, 2],
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
        """Innate Spellcasting: The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast ..."""
        return "The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast the following spells, requiring no material components:At will: druidcraft3/day each: entangle, good"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast ..."""
        return "The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast the following spells, requiring no material components:At will: druidcraft3/day each: entangle, good"

