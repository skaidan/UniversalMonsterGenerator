# bases1/mage.py
"""
Mage creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mage
"""
from creature_base import GlobalCreatureBaseClass


class Mage(GlobalCreatureBaseClass):
    """
    Mage creature
    Size: Medium, Type: humanoid (any race), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 40,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), any alignment",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['spellcasting'])

    def spellcasting(self) -> str:
        """Spellcasting: The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 ..."""
        return "The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:Cantrips (at will): fi"
    def spellcasting(self) -> str:
        """Spellcasting: The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 ..."""
        return "The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:Cantrips (at will): fi"

