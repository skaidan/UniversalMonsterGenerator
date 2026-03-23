# bases1/scout.py
"""
Scout creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scout
"""
from creature_base import GlobalCreatureBaseClass


class Scout(GlobalCreatureBaseClass):
    """
    Scout creature
    Size: Medium, Type: humanoid (any race), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 16,
        "min_level": 2,
        "level": 2,
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
        "type": "humanoid (any race), any alignment",
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
        self.abilities.extend(['keen_hearing_and_sight'])

    def keen_hearing_and_sight(self) -> str:
        """Keen Hearing and Sight: The scout has advantage on Wisdom (Perception) checks that rely on hearing or sight.ActionsMultiatta..."""
        return "The scout has advantage on Wisdom (Perception) checks that rely on hearing or sight.ActionsMultiattack. The scout makes two melee attacks or two ranged attacks.Shortsword. Melee Weapon Attack: +4 to h"
    def keen_hearing_and_sight(self) -> str:
        """Keen Hearing and Sight: The scout has advantage on Wisdom (Perception) checks that rely on hearing or sight.ActionsMultiatta..."""
        return "The scout has advantage on Wisdom (Perception) checks that rely on hearing or sight.ActionsMultiattack. The scout makes two melee attacks or two ranged attacks.Shortsword. Melee Weapon Attack: +4 to h"

