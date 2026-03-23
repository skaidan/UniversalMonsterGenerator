# bases1/githzerai-monk.py
"""
GithzeraiMonk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githzerai-monk
"""
from creature_base import GlobalCreatureBaseClass


class GithzeraiMonk(GlobalCreatureBaseClass):
    """
    GithzeraiMonk creature
    Size: Medium, Type: humanoid (Gith), lawful neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 38,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Gith), lawful neutral",
        "hit_points_up": [3, 3, 3],
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
        """Innate Spellcasting (Psionics): The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, re..."""
        return "The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: feather fall, jump, see "
    def innate_spellcasting_psionics(self) -> str:
        """Innate Spellcasting (Psionics): The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, re..."""
        return "The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: feather fall, jump, see "

