# bases1/killer-whale.py
"""
KillerWhale creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=killer-whale
"""
from creature_base import GlobalCreatureBaseClass


class KillerWhale(GlobalCreatureBaseClass):
    """
    KillerWhale creature
    Size: Huge, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 90,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast, unaligned",
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
        self.abilities.extend(['echolocation'])

    def echolocation(self) -> str:
        """Echolocation: The whale can't use its blindsight while deafened.Hold Breath. The whale can hold its breath for 30 ..."""
        return "The whale can't use its blindsight while deafened.Hold Breath. The whale can hold its breath for 30 minutes.Keen Hearing. The whale has advantage on Wisdom (Perception) checks that rely on hearing.Act"
    def echolocation(self) -> str:
        """Echolocation: The whale can't use its blindsight while deafened.Hold Breath. The whale can hold its breath for 30 ..."""
        return "The whale can't use its blindsight while deafened.Hold Breath. The whale can hold its breath for 30 minutes.Keen Hearing. The whale has advantage on Wisdom (Perception) checks that rely on hearing.Act"

