# bases1/hezrou.py
"""
Hezrou creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hezrou
"""
from creature_base import GlobalCreatureBaseClass


class Hezrou(GlobalCreatureBaseClass):
    """
    Hezrou creature
    Size: Large, Type: fiend (Demon), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 136,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend (Demon), chaotic evil",
        "hit_points_up": [13, 13, 13],
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
        """Magic Resistance: The hezrou has advantage on saving throws against spells and other magical effects.Stench. Any creat..."""
        return "The hezrou has advantage on saving throws against spells and other magical effects.Stench. Any creature that starts its turn within 10 feet of the hezrou must succeed on a DC 14 Constitution saving th"
    def magic_resistance(self) -> str:
        """Magic Resistance: The hezrou has advantage on saving throws against spells and other magical effects.Stench. Any creat..."""
        return "The hezrou has advantage on saving throws against spells and other magical effects.Stench. Any creature that starts its turn within 10 feet of the hezrou must succeed on a DC 14 Constitution saving th"

