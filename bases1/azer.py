# bases1/azer.py
"""
Azer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=azer
"""
from creature_base import GlobalCreatureBaseClass


class Azer(GlobalCreatureBaseClass):
    """
    Azer creature
    Size: Medium, Type: elemental, lawful neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 39,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "elemental, lawful neutral",
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
        self.abilities.extend(['heated_body'])

    def heated_body(self) -> str:
        """Heated Body: A creature that touches the azer or hits it with a melee attack while within 5 feet of it takes 5 (1..."""
        return "A creature that touches the azer or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage.Heated Weapons. When the azer hits with a metal melee weapon, it deals an extra 3 ("
    def heated_body(self) -> str:
        """Heated Body: A creature that touches the azer or hits it with a melee attack while within 5 feet of it takes 5 (1..."""
        return "A creature that touches the azer or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage.Heated Weapons. When the azer hits with a metal melee weapon, it deals an extra 3 ("

