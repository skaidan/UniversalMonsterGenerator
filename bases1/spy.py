# bases1/spy.py
"""
Spy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spy
"""
from creature_base import GlobalCreatureBaseClass


class Spy(GlobalCreatureBaseClass):
    """
    Spy creature
    Size: Medium, Type: humanoid (any race), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 27,
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
        "type": "humanoid (any race), any alignment",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['cunning_action'])

    def cunning_action(self) -> str:
        """Cunning Action: On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action.Sne..."""
        return "On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action.Sneak Attack (1/Turn). The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack"
    def cunning_action(self) -> str:
        """Cunning Action: On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action.Sne..."""
        return "On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action.Sneak Attack (1/Turn). The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack"

