# bases1/iron-golem.py
"""
IronGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=iron-golem
"""
from creature_base import GlobalCreatureBaseClass


class IronGolem(GlobalCreatureBaseClass):
    """
    IronGolem creature
    Size: Large, Type: construct, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 210,
        "min_level": 17,
        "level": 17,
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
        "type": "construct, unaligned",
        "hit_points_up": [21, 21, 21],
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
        self.abilities.extend(['fire_absorption'])

    def fire_absorption(self) -> str:
        """Fire Absorption: Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of h..."""
        return "Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of hit points equal to the fire damage dealt.Immutable Form. The golem is immune to any spell or effect "
    def fire_absorption(self) -> str:
        """Fire Absorption: Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of h..."""
        return "Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of hit points equal to the fire damage dealt.Immutable Form. The golem is immune to any spell or effect "

