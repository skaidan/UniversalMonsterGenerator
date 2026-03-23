# bases1/goblin-boss.py
"""
GoblinBoss creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=goblin-boss
"""
from creature_base import GlobalCreatureBaseClass


class GoblinBoss(GlobalCreatureBaseClass):
    """
    GoblinBoss creature
    Size: Small, Type: humanoid (Goblinoid), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 21,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "humanoid (Goblinoid), neutral evil",
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
        self.abilities.extend(['nimble_escape'])

    def nimble_escape(self) -> str:
        """Nimble Escape: The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsMulti..."""
        return "The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsMultiattack. The goblin makes two attacks with its scimitar. The second attack has disadvantage.Scimitar."
    def nimble_escape(self) -> str:
        """Nimble Escape: The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsMulti..."""
        return "The goblin can take the Disengage or Hide action as a bonus action on each of its turns.ActionsMultiattack. The goblin makes two attacks with its scimitar. The second attack has disadvantage.Scimitar."

