# bases1/swarm-of-poisonous-snakes.py
"""
SwarmOfPoisonousSnakes creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-poisonous-snakes
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfPoisonousSnakes(GlobalCreatureBaseClass):
    """
    SwarmOfPoisonousSnakes creature
    Size: Tiny, Type: snake. The swarm can't regain hit points or gain temporary hit points.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 36,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "snake. The swarm can't regain hit points or gain temporary hit points.",
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
        self.abilities.extend(['swarm'])

    def swarm(self) -> str:
        """Swarm: The swarm can occupy another creature's space and vice versa, and the swarm can move through any ope..."""
        return "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny snake. The swarm can't regain hit points or gain temporary hit points.A"
    def swarm(self) -> str:
        """Swarm: The swarm can occupy another creature's space and vice versa, and the swarm can move through any ope..."""
        return "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny snake. The swarm can't regain hit points or gain temporary hit points.A"

