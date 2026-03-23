# bases1/salamander.py
"""
Salamander creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=salamander
"""
from creature_base import GlobalCreatureBaseClass


class Salamander(GlobalCreatureBaseClass):
    """
    Salamander creature
    Size: Large, Type: elemental, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 90,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "elemental, neutral evil",
        "hit_points_up": [9, 9, 9],
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
        """Heated Body: A creature that touches the salamander or hits it with a melee attack while within 5 feet of it take..."""
        return "A creature that touches the salamander or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.Heated Weapons. Any metal melee weapon the salamander wields deals an extra 3 "
    def heated_body(self) -> str:
        """Heated Body: A creature that touches the salamander or hits it with a melee attack while within 5 feet of it take..."""
        return "A creature that touches the salamander or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.Heated Weapons. Any metal melee weapon the salamander wields deals an extra 3 "

