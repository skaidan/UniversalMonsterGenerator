# bases1/cultist.py
"""
Cultist creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cultist
"""
from creature_base import GlobalCreatureBaseClass


class Cultist(GlobalCreatureBaseClass):
    """
    Cultist creature
    Size: Medium, Type: humanoid (any race), any non-good alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 9,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), any non-good alignment",
        "hit_points_up": [1, 1, 1],
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
        """Dark Devotion: The cultist has advantage on saving throws against being charmed or frightened.ActionsScimitar. Mele..."""
        return "The cultist has advantage on saving throws against being charmed or frightened.ActionsScimitar. Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) slashing damage.Cultists swe"
    def dark_devotion(self) -> str:
        """Dark Devotion: The cultist has advantage on saving throws against being charmed or frightened.ActionsScimitar. Mele..."""
        return "The cultist has advantage on saving throws against being charmed or frightened.ActionsScimitar. Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) slashing damage.Cultists swe"

