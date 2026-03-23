# bases1/pixie.py
"""
Pixie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pixie
"""
from creature_base import GlobalCreatureBaseClass


class Pixie(GlobalCreatureBaseClass):
    """
    Pixie creature
    Size: Tiny, Type: fey, neutral good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 1,
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
        "type": "fey, neutral good",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The pixie has advantage on saving throws against spells and other magical effects.Innate Spellcastin..."""
        return "The pixie has advantage on saving throws against spells and other magical effects.Innate Spellcasting. The pixie's innate spellcasting ability is Charisma (spell save DC 12). It can innately cast the "
    def magic_resistance(self) -> str:
        """Magic Resistance: The pixie has advantage on saving throws against spells and other magical effects.Innate Spellcastin..."""
        return "The pixie has advantage on saving throws against spells and other magical effects.Innate Spellcasting. The pixie's innate spellcasting ability is Charisma (spell save DC 12). It can innately cast the "

