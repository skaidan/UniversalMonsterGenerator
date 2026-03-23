# bases1/fire-snake.py
"""
FireSnake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-snake
"""
from creature_base import GlobalCreatureBaseClass


class FireSnake(GlobalCreatureBaseClass):
    """
    FireSnake creature
    Size: Medium, Type: elemental, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
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
        "type": "elemental, neutral evil",
        "hit_points_up": [2, 2, 2],
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
        """Heated Body: A creature that touches the snake or hits it with a melee attack while within 5 feet of it takes 3 (..."""
        return "A creature that touches the snake or hits it with a melee attack while within 5 feet of it takes 3 (1d6) fire damage.ActionsMultiattack. The snake makes two attacks: one with its bite and one with its"
    def heated_body(self) -> str:
        """Heated Body: A creature that touches the snake or hits it with a melee attack while within 5 feet of it takes 3 (..."""
        return "A creature that touches the snake or hits it with a melee attack while within 5 feet of it takes 3 (1d6) fire damage.ActionsMultiattack. The snake makes two attacks: one with its bite and one with its"

