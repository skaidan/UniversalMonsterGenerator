# bases1/assassin.py
"""
Assassin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=assassin
"""
from creature_base import GlobalCreatureBaseClass


class Assassin(GlobalCreatureBaseClass):
    """
    Assassin creature
    Size: Medium, Type: humanoid (any race), any non-good alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 78,
        "min_level": 9,
        "level": 9,
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
        "type": "humanoid (any race), any non-good alignment",
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
        self.abilities.extend(['assassinate'])

    def assassinate(self) -> str:
        """Assassinate: During its first turn, the assassin has advantage on attack rolls against any creature that hasn't t..."""
        return "During its first turn, the assassin has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critical hit.Evasion. If "
    def assassinate(self) -> str:
        """Assassinate: During its first turn, the assassin has advantage on attack rolls against any creature that hasn't t..."""
        return "During its first turn, the assassin has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critical hit.Evasion. If "

