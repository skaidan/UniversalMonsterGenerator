# bases1/gas-spore.py
"""
GasSpore creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gas-spore
"""
from creature_base import GlobalCreatureBaseClass


class GasSpore(GlobalCreatureBaseClass):
    """
    GasSpore creature
    Size: Tiny, Type: gas spores that grow to full size in 7 days.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 1,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 5,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "gas spores that grow to full size in 7 days.",
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
        self.abilities.extend(['death_burst'])

    def death_burst(self) -> str:
        """Death Burst: The gas spore explodes when it drops to 0 hit points. Each creature within 20 feet of it must succee..."""
        return "The gas spore explodes when it drops to 0 hit points. Each creature within 20 feet of it must succeed on a DC 15 Constitution saving throw or take 10 (3d6) poison damage and become infected with a dis"
    def death_burst(self) -> str:
        """Death Burst: The gas spore explodes when it drops to 0 hit points. Each creature within 20 feet of it must succee..."""
        return "The gas spore explodes when it drops to 0 hit points. Each creature within 20 feet of it must succeed on a DC 15 Constitution saving throw or take 10 (3d6) poison damage and become infected with a dis"

