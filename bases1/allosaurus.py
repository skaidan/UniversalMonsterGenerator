# bases1/allosaurus.py
"""
Allosaurus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=allosaurus
"""
from creature_base import GlobalCreatureBaseClass


class Allosaurus(GlobalCreatureBaseClass):
    """
    Allosaurus creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 51,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['pounce'])

    def pounce(self) -> str:
        """Pounce: If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw att..."""
        return "If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone."
    def pounce(self) -> str:
        """Pounce: If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw att..."""
        return "If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone."

