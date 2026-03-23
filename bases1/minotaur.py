# bases1/minotaur.py
"""
Minotaur creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minotaur
"""
from creature_base import GlobalCreatureBaseClass


class Minotaur(GlobalCreatureBaseClass):
    """
    Minotaur creature
    Size: Large, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 76,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, chaotic evil",
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
        self.abilities.extend(['charge'])

    def charge(self) -> str:
        """Charge: If the minotaur moves at least 10 feet straight toward a target and then hits it with a gore attack ..."""
        return "If the minotaur moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it"
    def charge(self) -> str:
        """Charge: If the minotaur moves at least 10 feet straight toward a target and then hits it with a gore attack ..."""
        return "If the minotaur moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it"

