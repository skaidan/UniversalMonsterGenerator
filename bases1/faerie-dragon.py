# bases1/faerie-dragon.py
"""
FaerieDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=faerie-dragon
"""
from creature_base import GlobalCreatureBaseClass


class FaerieDragon(GlobalCreatureBaseClass):
    """
    FaerieDragon creature
    Size: Tiny, Type: dragon, chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 14,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "dragon, chaotic good",
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
        self.abilities.extend(['innate_spellcasting'])

    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The dragon's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast a numb..."""
        return "The dragon's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast a number of spells, requiring no material components. As the dragon ages and changes color, it gains addit"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The dragon's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast a numb..."""
        return "The dragon's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast a number of spells, requiring no material components. As the dragon ages and changes color, it gains addit"

