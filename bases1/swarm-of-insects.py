# bases1/swarm-of-insects.py
"""
SwarmOfInsects creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-insects
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfInsects(GlobalCreatureBaseClass):
    """
    SwarmOfInsects creature
    Size: Tiny, Type: insect. The swarm can't regain hit points or gain temporary hit points.
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
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "insect. The swarm can't regain hit points or gain temporary hit points.",
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
        self.abilities.extend(['swarm'])

    def swarm(self) -> str:
        """Swarm: The swarm can occupy another creature's space and vice versa, and the swarm can move through any ope..."""
        return "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."
    def swarm(self) -> str:
        """Swarm: The swarm can occupy another creature's space and vice versa, and the swarm can move through any ope..."""
        return "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."

