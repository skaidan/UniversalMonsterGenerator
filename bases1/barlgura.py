# bases1/barlgura.py
"""
Barlgura creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=barlgura
"""
from creature_base import GlobalCreatureBaseClass


class Barlgura(GlobalCreatureBaseClass):
    """
    Barlgura creature
    Size: Large, Type: fiend (Demon), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 68,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend (Demon), chaotic evil",
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
        self.abilities.extend(['innate_spellcasting'])

    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The barlgura's spellcasting ability is Wisdom (spell save DC 13). The barlgura can innately cast the..."""
        return "The barlgura's spellcasting ability is Wisdom (spell save DC 13). The barlgura can innately cast the following spells, requiring no material components:1/day each: entangle, phantasmal force2/day each"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The barlgura's spellcasting ability is Wisdom (spell save DC 13). The barlgura can innately cast the..."""
        return "The barlgura's spellcasting ability is Wisdom (spell save DC 13). The barlgura can innately cast the following spells, requiring no material components:1/day each: entangle, phantasmal force2/day each"

