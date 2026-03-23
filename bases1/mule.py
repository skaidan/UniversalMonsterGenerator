# bases1/mule.py
"""
Mule creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mule
"""
from creature_base import GlobalCreatureBaseClass


class Mule(GlobalCreatureBaseClass):
    """
    Mule creature
    Size: Large, Type: animal for the purpose of determining its carrying capacity.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
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
        "size": "Large",
        "type": "animal for the purpose of determining its carrying capacity.",
        "hit_points_up": [1, 1, 1],
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
        self.abilities.extend(['beast_of_burden'])

    def beast_of_burden(self) -> str:
        """Beast of Burden: The mule is considered to be a Large animal for the purpose of determining its carrying capacity.Sur..."""
        return "The mule is considered to be a Large animal for the purpose of determining its carrying capacity.Sure-Footed. The mule has advantage on Strength and Dexterity saving throws made against effects that w"
    def beast_of_burden(self) -> str:
        """Beast of Burden: The mule is considered to be a Large animal for the purpose of determining its carrying capacity.Sur..."""
        return "The mule is considered to be a Large animal for the purpose of determining its carrying capacity.Sure-Footed. The mule has advantage on Strength and Dexterity saving throws made against effects that w"

