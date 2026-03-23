# bases1/orog.py
"""
Orog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orog
"""
from creature_base import GlobalCreatureBaseClass


class Orog(GlobalCreatureBaseClass):
    """
    Orog creature
    Size: Medium, Type: humanoid (Orc), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 42,
        "min_level": 3,
        "level": 3,
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
        "type": "humanoid (Orc), chaotic evil",
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
        self.abilities.extend(['aggressive'])

    def aggressive(self) -> str:
        """Aggressive: As a bonus action, the orog can move up to its speed toward a hostile creature that it can see.Actio..."""
        return "As a bonus action, the orog can move up to its speed toward a hostile creature that it can see.ActionsMultiattack. The orog makes two greataxe attacks.Greataxe. Melee Weapon Attack: +6 to hit, reach 5"
    def aggressive(self) -> str:
        """Aggressive: As a bonus action, the orog can move up to its speed toward a hostile creature that it can see.Actio..."""
        return "As a bonus action, the orog can move up to its speed toward a hostile creature that it can see.ActionsMultiattack. The orog makes two greataxe attacks.Greataxe. Melee Weapon Attack: +6 to hit, reach 5"

