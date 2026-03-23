# bases1/swarm-of-quippers.py
"""
SwarmOfQuippers creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-quippers
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfQuippers(GlobalCreatureBaseClass):
    """
    SwarmOfQuippers creature
    Size: Tiny, Type: quipper. The swarm can't regain hit points or gain temporary hit points.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 28,
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
        "size": "Tiny",
        "type": "quipper. The swarm can't regain hit points or gain temporary hit points.",
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
        self.abilities.extend(['blood_frenzy'])

    def blood_frenzy(self) -> str:
        """Blood Frenzy: The swarm has advantage on melee attack rolls against any creature that doesn't have all its hit poi..."""
        return "The swarm has advantage on melee attack rolls against any creature that doesn't have all its hit points.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move thro"
    def blood_frenzy(self) -> str:
        """Blood Frenzy: The swarm has advantage on melee attack rolls against any creature that doesn't have all its hit poi..."""
        return "The swarm has advantage on melee attack rolls against any creature that doesn't have all its hit points.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move thro"

