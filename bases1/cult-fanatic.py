# bases1/cult-fanatic.py
"""
CultFanatic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cult-fanatic
"""
from creature_base import GlobalCreatureBaseClass


class CultFanatic(GlobalCreatureBaseClass):
    """
    CultFanatic creature
    Size: Medium, Type: humanoid (any race), any non-good alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
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
        "type": "humanoid (any race), any non-good alignment",
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
        self.abilities.extend(['dark_devotion'])

    def dark_devotion(self) -> str:
        """Dark Devotion: The fanatic has advantage on saving throws against being charmed or frightened.Spellcasting. The fan..."""
        return "The fanatic has advantage on saving throws against being charmed or frightened.Spellcasting. The fanatic is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 11, +3 to hit wit"
    def dark_devotion(self) -> str:
        """Dark Devotion: The fanatic has advantage on saving throws against being charmed or frightened.Spellcasting. The fan..."""
        return "The fanatic has advantage on saving throws against being charmed or frightened.Spellcasting. The fanatic is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 11, +3 to hit wit"

