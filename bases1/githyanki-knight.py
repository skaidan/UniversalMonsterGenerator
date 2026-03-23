# bases1/githyanki-knight.py
"""
GithyankiKnight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githyanki-knight
"""
from creature_base import GlobalCreatureBaseClass


class GithyankiKnight(GlobalCreatureBaseClass):
    """
    GithyankiKnight creature
    Size: Medium, Type: humanoid (Gith), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 91,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Gith), lawful evil",
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
        self.abilities.extend(['innate_spellcasting_psionics'])

    def innate_spellcasting_psionics(self) -> str:
        """Innate Spellcasting (Psionics): The githyanki's innate spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell ..."""
        return "The githyanki's innate spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no components:At will: mage hand (the"
    def innate_spellcasting_psionics(self) -> str:
        """Innate Spellcasting (Psionics): The githyanki's innate spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell ..."""
        return "The githyanki's innate spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no components:At will: mage hand (the"

