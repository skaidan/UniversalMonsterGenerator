# bases1/empyrean.py
"""
Empyrean creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=empyrean
"""
from creature_base import GlobalCreatureBaseClass


class Empyrean(GlobalCreatureBaseClass):
    """
    Empyrean creature
    Size: Huge, Type: celestial (Titan), chaotic good (75 %) or neutral evil (25 %)
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 313,
        "min_level": 24,
        "level": 24,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 22,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "celestial (Titan), chaotic good (75 %) or neutral evil (25 %)",
        "hit_points_up": [31, 31, 31],
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
        """Innate Spellcasting: The empyrean's innate spellcasting ability is Charisma (spell save DC 23, +15 to hit with spell atta..."""
        return "The empyrean's innate spellcasting ability is Charisma (spell save DC 23, +15 to hit with spell attacks).It can innately cast the following spells, requiring no material components:At will: greater re"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The empyrean's innate spellcasting ability is Charisma (spell save DC 23, +15 to hit with spell atta..."""
        return "The empyrean's innate spellcasting ability is Charisma (spell save DC 23, +15 to hit with spell attacks).It can innately cast the following spells, requiring no material components:At will: greater re"

