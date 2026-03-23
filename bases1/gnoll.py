# bases1/gnoll.py
"""
Gnoll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll
"""
from creature_base import GlobalCreatureBaseClass


class Gnoll(GlobalCreatureBaseClass):
    """
    Gnoll creature
    Size: Medium, Type: humanoid (Gnoll), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
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
        "size": "Medium",
        "type": "humanoid (Gnoll), chaotic evil",
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
        self.abilities.extend(['rampage'])

    def rampage(self) -> str:
        """Rampage: When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can tak..."""
        return "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack.ActionsBite. Melee Weapon Attac"
    def rampage(self) -> str:
        """Rampage: When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can tak..."""
        return "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack.ActionsBite. Melee Weapon Attac"

