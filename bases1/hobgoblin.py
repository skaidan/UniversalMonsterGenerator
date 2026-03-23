# bases1/hobgoblin.py
"""
Hobgoblin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin
"""
from creature_base import GlobalCreatureBaseClass


class Hobgoblin(GlobalCreatureBaseClass):
    """
    Hobgoblin creature
    Size: Medium, Type: humanoid (Goblinoid), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Goblinoid), lawful evil",
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
        self.abilities.extend(['martial_advantage'])

    def martial_advantage(self) -> str:
        """Martial Advantage: Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon at..."""
        return "Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated.ActionsL"
    def martial_advantage(self) -> str:
        """Martial Advantage: Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon at..."""
        return "Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated.ActionsL"

