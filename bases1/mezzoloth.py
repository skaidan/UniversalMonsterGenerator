# bases1/mezzoloth.py
"""
Mezzoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mezzoloth
"""
from creature_base import GlobalCreatureBaseClass


class Mezzoloth(GlobalCreatureBaseClass):
    """
    Mezzoloth creature
    Size: Medium, Type: fiend (Yugoloth), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 75,
        "min_level": 6,
        "level": 6,
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
        "type": "fiend (Yugoloth), neutral evil",
        "hit_points_up": [7, 7, 7],
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
        """Innate Spellcasting: The mezzoloth's innate spellcasting ability is Charisma (spell save DC 11). The mezzoloth can innate..."""
        return "The mezzoloth's innate spellcasting ability is Charisma (spell save DC 11). The mezzoloth can innately cast the following spells, requiring no material components:2/day each: darkness, dispel magic1/d"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The mezzoloth's innate spellcasting ability is Charisma (spell save DC 11). The mezzoloth can innate..."""
        return "The mezzoloth's innate spellcasting ability is Charisma (spell save DC 11). The mezzoloth can innately cast the following spells, requiring no material components:2/day each: darkness, dispel magic1/d"

