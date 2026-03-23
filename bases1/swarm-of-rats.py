# bases1/swarm-of-rats.py
"""
SwarmOfRats creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-rats
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfRats(GlobalCreatureBaseClass):
    """
    SwarmOfRats creature
    Size: Tiny, Type: rat. The swarm can't regain hit points or gain temporary hit points.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 24,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "rat. The swarm can't regain hit points or gain temporary hit points.",
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
        self.abilities.extend(['keen_smell'])

    def keen_smell(self) -> str:
        """Keen Smell: The swarm has advantage on Wisdom (Perception) checks that rely on smell.Swarm. The swarm can occupy..."""
        return "The swarm has advantage on Wisdom (Perception) checks that rely on smell.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough fo"
    def keen_smell(self) -> str:
        """Keen Smell: The swarm has advantage on Wisdom (Perception) checks that rely on smell.Swarm. The swarm can occupy..."""
        return "The swarm has advantage on Wisdom (Perception) checks that rely on smell.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough fo"

