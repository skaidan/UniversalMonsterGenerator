# bases1/berserker.py
"""
Berserker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=berserker
"""
from creature_base import GlobalCreatureBaseClass


class Berserker(GlobalCreatureBaseClass):
    """
    Berserker creature
    Size: Medium, Type: humanoid (any race), any chaotic alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 67,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), any chaotic alignment",
        "hit_points_up": [6, 6, 6],
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
        self.abilities.extend(['reckless'])

    def reckless(self) -> str:
        """Reckless: At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during t..."""
        return "At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn.ActionsGreatax"
    def reckless(self) -> str:
        """Reckless: At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during t..."""
        return "At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn.ActionsGreatax"

