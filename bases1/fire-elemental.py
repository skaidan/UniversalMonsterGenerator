# bases1/fire-elemental.py
"""
FireElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-elemental
"""
from creature_base import GlobalCreatureBaseClass


class FireElemental(GlobalCreatureBaseClass):
    """
    FireElemental creature
    Size: Large, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 102,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "elemental, neutral",
        "hit_points_up": [10, 10, 10],
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
        self.abilities.extend(['fire_form'])

    def fire_form(self) -> str:
        """Fire Form: The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that t..."""
        return "The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire da"
    def fire_form(self) -> str:
        """Fire Form: The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that t..."""
        return "The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire da"

