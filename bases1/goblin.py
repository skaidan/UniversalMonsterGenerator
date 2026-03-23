# bases1/goblin.py
"""
Goblin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=goblin
"""
from creature_base import GlobalCreatureBaseClass


class Goblin(GlobalCreatureBaseClass):
    """
    Goblin creature
    Size: Small, Type: humanoid (Goblinoid), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 7,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "humanoid (Goblinoid), neutral evil",
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
        self.abilities.extend(['nimble_escape'])

    def nimble_escape(self) -> str:
        """Nimble Escape: The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsScimi..."""
        return "The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsScimitar. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.Short"
    def nimble_escape(self) -> str:
        """Nimble Escape: The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsScimi..."""
        return "The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsScimitar. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.Short"

