# bases1/ettin.py
"""
Ettin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ettin
"""
from creature_base import GlobalCreatureBaseClass


class Ettin(GlobalCreatureBaseClass):
    """
    Ettin creature
    Size: Large, Type: giant, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 85,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "giant, chaotic evil",
        "hit_points_up": [8, 8, 8],
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
        self.abilities.extend(['two_heads'])

    def two_heads(self) -> str:
        """Two Heads: The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, ch..."""
        return "The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned and knocked unconscious.Wakeful. When one of the ettin's heads "
    def two_heads(self) -> str:
        """Two Heads: The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, ch..."""
        return "The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned and knocked unconscious.Wakeful. When one of the ettin's heads "

