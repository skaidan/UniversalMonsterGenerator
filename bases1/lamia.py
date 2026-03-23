# bases1/lamia.py
"""
Lamia creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lamia
"""
from creature_base import GlobalCreatureBaseClass


class Lamia(GlobalCreatureBaseClass):
    """
    Lamia creature
    Size: Large, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 97,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, chaotic evil",
        "hit_points_up": [9, 9, 9],
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
        """Innate Spellcasting: The lamia's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the fol..."""
        return "The lamia's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the following spells, requiring no material components.At will: disguise self (any humanoid form), major im"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The lamia's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the fol..."""
        return "The lamia's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the following spells, requiring no material components.At will: disguise self (any humanoid form), major im"

