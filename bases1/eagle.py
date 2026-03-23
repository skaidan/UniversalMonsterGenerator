# bases1/eagle.py
"""
Eagle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=eagle
"""
from creature_base import GlobalCreatureBaseClass


class Eagle(GlobalCreatureBaseClass):
    """
    Eagle creature
    Size: Small, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 3,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "beast, unaligned",
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
        self.abilities.extend(['keen_sight'])

    def keen_sight(self) -> str:
        """Keen Sight: The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsTalons. Melee Weapon..."""
        return "The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsTalons. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.Monster Manual (SRD)
	"
    def keen_sight(self) -> str:
        """Keen Sight: The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsTalons. Melee Weapon..."""
        return "The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsTalons. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.Monster Manual (SRD)
	"

