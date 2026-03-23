# bases1/flesh-golem.py
"""
FleshGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flesh-golem
"""
from creature_base import GlobalCreatureBaseClass


class FleshGolem(GlobalCreatureBaseClass):
    """
    FleshGolem creature
    Size: Medium, Type: construct, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 93,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 9,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "construct, neutral",
        "hit_points_up": [9, 9, 9],
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
        self.abilities.extend(['berserk'])

    def berserk(self) -> str:
        """Berserk: Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes be..."""
        return "Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no "
    def berserk(self) -> str:
        """Berserk: Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes be..."""
        return "Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no "

