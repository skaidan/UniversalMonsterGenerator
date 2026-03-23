# bases1/hobgoblin-iron-shadow.py
"""
HobgoblinIronShadow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin-iron-shadow
"""
from creature_base import GlobalCreatureBaseClass


class HobgoblinIronShadow(GlobalCreatureBaseClass):
    """
    HobgoblinIronShadow creature
    Size: Medium, Type: Fey (Goblinoid), typically Lawful Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 32,
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
        "type": "Fey (Goblinoid), typically Lawful Neutral",
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
        # Add creature-specific abilities
        self.abilities.extend(['unarmored_defense'])

    def unarmored_defense(self) -> str:
        """Unarmored Defense: While the hobgoblin is wearing no armor and wielding no shield, its AC includes its Wisdom modifier...."""
        return "While the hobgoblin is wearing no armor and wielding no shield, its AC includes its Wisdom modifier.ActionsMultiattack. The hobgoblin makes four attacks, each of which can be an Unarmed Strike or a Da"

