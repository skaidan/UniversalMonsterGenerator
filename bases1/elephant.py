# bases1/elephant.py
"""
Elephant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elephant
"""
from creature_base import GlobalCreatureBaseClass


class Elephant(GlobalCreatureBaseClass):
    """
    Elephant creature
    Size: Huge, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 76,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast, unaligned",
        "hit_points_up": [7, 7, 7],
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
        self.abilities.extend(['trampling_charge'])

    def trampling_charge(self) -> str:
        """Trampling Charge: If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attac..."""
        return "If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. I"
    def trampling_charge(self) -> str:
        """Trampling Charge: If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attac..."""
        return "If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. I"

