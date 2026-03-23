# bases1/roc.py
"""
Roc creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=roc
"""
from creature_base import GlobalCreatureBaseClass


class Roc(GlobalCreatureBaseClass):
    """
    Roc creature
    Size: Gargantuan, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 248,
        "min_level": 12,
        "level": 12,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "monstrosity, unaligned",
        "hit_points_up": [24, 24, 24],
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
        """Keen Sight: The roc has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The roc m..."""
        return "The roc has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The roc makes two attacks: one with its beak and one with its talons.Beak. Melee Weapon Attack: +13 to hit, r"
    def keen_sight(self) -> str:
        """Keen Sight: The roc has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The roc m..."""
        return "The roc has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The roc makes two attacks: one with its beak and one with its talons.Beak. Melee Weapon Attack: +13 to hit, r"

