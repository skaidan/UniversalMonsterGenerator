# bases1/rakshasa.py
"""
Rakshasa creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rakshasa
"""
from creature_base import GlobalCreatureBaseClass


class Rakshasa(GlobalCreatureBaseClass):
    """
    Rakshasa creature
    Size: Medium, Type: fiend, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 110,
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
        "size": "Medium",
        "type": "fiend, lawful evil",
        "hit_points_up": [11, 11, 11],
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
        self.abilities.extend(['limited_magic_immunity'])

    def limited_magic_immunity(self) -> str:
        """Limited Magic Immunity: The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be. I..."""
        return "The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has advantage on saving throws against all other spells and magical effects.Innate Spellcasting. T"
    def limited_magic_immunity(self) -> str:
        """Limited Magic Immunity: The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be. I..."""
        return "The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has advantage on saving throws against all other spells and magical effects.Innate Spellcasting. T"

