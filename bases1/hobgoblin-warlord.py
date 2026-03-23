# bases1/hobgoblin-warlord.py
"""
HobgoblinWarlord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin-warlord
"""
from creature_base import GlobalCreatureBaseClass


class HobgoblinWarlord(GlobalCreatureBaseClass):
    """
    HobgoblinWarlord creature
    Size: Large, Type: or smaller, it must succeed on a DC 14 Strength saving throw or be knocked prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 97,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller, it must succeed on a DC 14 Strength saving throw or be knocked prone.",
        "hit_points_up": [9, 9, 9],
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
        """Martial Advantage: Once per turn, the hobgoblin can deal an extra 14 (4d6) damage to a creature it hits with a weapon a..."""
        return "Once per turn, the hobgoblin can deal an extra 14 (4d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated.Actions"
    def martial_advantage(self) -> str:
        """Martial Advantage: Once per turn, the hobgoblin can deal an extra 14 (4d6) damage to a creature it hits with a weapon a..."""
        return "Once per turn, the hobgoblin can deal an extra 14 (4d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated.Actions"

