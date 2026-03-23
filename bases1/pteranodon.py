# bases1/pteranodon.py
"""
Pteranodon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pteranodon
"""
from creature_base import GlobalCreatureBaseClass


class Pteranodon(GlobalCreatureBaseClass):
    """
    Pteranodon creature
    Size: Medium, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
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
        self.abilities.extend(['flyby'])

    def flyby(self) -> str:
        """Flyby: The pteranodon doesn't provoke an opportunity attack when it flies out of an enemy's reach.ActionsBi..."""
        return "The pteranodon doesn't provoke an opportunity attack when it flies out of an enemy's reach.ActionsBite. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.These "
    def flyby(self) -> str:
        """Flyby: The pteranodon doesn't provoke an opportunity attack when it flies out of an enemy's reach.ActionsBi..."""
        return "The pteranodon doesn't provoke an opportunity attack when it flies out of an enemy's reach.ActionsBite. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.These "

