# bases1/swarm-of-bats.py
"""
SwarmOfBats creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-bats
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfBats(GlobalCreatureBaseClass):
    """
    SwarmOfBats creature
    Size: Tiny, Type: bat. The swarm can't regain hit points or gain temporary hit points.
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
        "type": "bat. The swarm can't regain hit points or gain temporary hit points.",
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
        self.abilities.extend(['echolocation'])

    def echolocation(self) -> str:
        """Echolocation: The swarm can't use its blindsight while deafened.Keen Hearing. The swarm has advantage on Wisdom (P..."""
        return "The swarm can't use its blindsight while deafened.Keen Hearing. The swarm has advantage on Wisdom (Perception) checks that rely on hearing.Swarm. The swarm can occupy another creature's space and vice"
    def echolocation(self) -> str:
        """Echolocation: The swarm can't use its blindsight while deafened.Keen Hearing. The swarm has advantage on Wisdom (P..."""
        return "The swarm can't use its blindsight while deafened.Keen Hearing. The swarm has advantage on Wisdom (Perception) checks that rely on hearing.Swarm. The swarm can occupy another creature's space and vice"

