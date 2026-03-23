# bases1/bugbear.py
"""
Bugbear creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bugbear
"""
from creature_base import GlobalCreatureBaseClass


class Bugbear(GlobalCreatureBaseClass):
    """
    Bugbear creature
    Size: Medium, Type: humanoid (Goblinoid), chaotic evil
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
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Goblinoid), chaotic evil",
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
        self.abilities.extend(['brute'])

    def brute(self) -> str:
        """Brute: A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the atta..."""
        return "A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the attack).Surprise Attack. If the bugbear surprises a creature and hits it with an attack during the first"
    def brute(self) -> str:
        """Brute: A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the atta..."""
        return "A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the attack).Surprise Attack. If the bugbear surprises a creature and hits it with an attack during the first"

