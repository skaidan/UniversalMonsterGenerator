# bases1/storm-giant.py
"""
StormGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=storm-giant
"""
from creature_base import GlobalCreatureBaseClass


class StormGiant(GlobalCreatureBaseClass):
    """
    StormGiant creature
    Size: Huge, Type: giant, chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 230,
        "min_level": 14,
        "level": 14,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "giant, chaotic good",
        "hit_points_up": [23, 23, 23],
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The giant can breathe air and water.Innate Spellcasting. The giant's innate spellcasting ability is ..."""
        return "The giant can breathe air and water.Innate Spellcasting. The giant's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material compon"
    def amphibious(self) -> str:
        """Amphibious: The giant can breathe air and water.Innate Spellcasting. The giant's innate spellcasting ability is ..."""
        return "The giant can breathe air and water.Innate Spellcasting. The giant's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material compon"

