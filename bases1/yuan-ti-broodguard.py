# bases1/yuan-ti-broodguard.py
"""
YuanTiBroodguard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-broodguard
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiBroodguard(GlobalCreatureBaseClass):
    """
    YuanTiBroodguard creature
    Size: Medium, Type: Monstrosity, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 3,
        "level": 3,
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
        "type": "Monstrosity, typically Neutral Evil",
        "hit_points_up": [4, 4, 4],
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
        # Add creature-specific abilities
        self.abilities.extend(['reckless'])

    def reckless(self) -> str:
        """Reckless: At the start of its turn, the broodguard can gain advantage on all melee weapon attack rolls it make..."""
        return "At the start of its turn, the broodguard can gain advantage on all melee weapon attack rolls it makes during that turn, but attack rolls against it have advantage until the start of its next turn.Acti"

