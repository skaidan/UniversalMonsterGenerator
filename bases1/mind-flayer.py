# bases1/mind-flayer.py
"""
MindFlayer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mind-flayer
"""
from creature_base import GlobalCreatureBaseClass


class MindFlayer(GlobalCreatureBaseClass):
    """
    MindFlayer creature
    Size: Medium, Type: or smaller, it is grappled (escape DC 15) and must succeed on a DC 15 Intelligence saving throw or be stunned until this grapple ends.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 71,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, it is grappled (escape DC 15) and must succeed on a DC 15 Intelligence saving throw or be stunned until this grapple ends.",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The mind flayer has advantage on saving throws against spells and other magical effects.Innate Spell..."""
        return "The mind flayer has advantage on saving throws against spells and other magical effects.Innate Spellcasting (Psionics). The mind flayer's innate spellcasting ability is Intelligence (spell save DC 15)"
    def magic_resistance(self) -> str:
        """Magic Resistance: The mind flayer has advantage on saving throws against spells and other magical effects.Innate Spell..."""
        return "The mind flayer has advantage on saving throws against spells and other magical effects.Innate Spellcasting (Psionics). The mind flayer's innate spellcasting ability is Intelligence (spell save DC 15)"

