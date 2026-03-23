# bases1/nothic.py
"""
Nothic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nothic
"""
from creature_base import GlobalCreatureBaseClass


class Nothic(GlobalCreatureBaseClass):
    """
    Nothic creature
    Size: Medium, Type: aberration, neutral evil
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
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "aberration, neutral evil",
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
        self.abilities.extend(['keen_sight'])

    def keen_sight(self) -> str:
        """Keen Sight: The nothic has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The no..."""
        return "The nothic has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The nothic makes two claw attacks.Claw. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1"
    def keen_sight(self) -> str:
        """Keen Sight: The nothic has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The no..."""
        return "The nothic has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The nothic makes two claw attacks.Claw. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1"

