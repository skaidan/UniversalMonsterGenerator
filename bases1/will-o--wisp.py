# bases1/will-o--wisp.py
"""
WillOWisp creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=will-o--wisp
"""
from creature_base import GlobalCreatureBaseClass


class WillOWisp(GlobalCreatureBaseClass):
    """
    WillOWisp creature
    Size: Tiny, Type: undead, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "undead, chaotic evil",
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
        self.abilities.extend(['consume_life'])

    def consume_life(self) -> str:
        """Consume Life: As a bonus action, the will-o'-wisp can target one creature it can see within 5 feet of it that has ..."""
        return "As a bonus action, the will-o'-wisp can target one creature it can see within 5 feet of it that has 0 hit points and is still alive. The target must succeed on a DC 10 Constitution saving throw agains"
    def consume_life(self) -> str:
        """Consume Life: As a bonus action, the will-o'-wisp can target one creature it can see within 5 feet of it that has ..."""
        return "As a bonus action, the will-o'-wisp can target one creature it can see within 5 feet of it that has 0 hit points and is still alive. The target must succeed on a DC 10 Constitution saving throw agains"

