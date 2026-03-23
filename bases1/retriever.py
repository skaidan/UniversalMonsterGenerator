# bases1/retriever.py
"""
Retriever creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=retriever
"""
from creature_base import GlobalCreatureBaseClass


class Retriever(GlobalCreatureBaseClass):
    """
    Retriever creature
    Size: Medium, Type: or smaller, the retriever can pick it up as part of the retriever's move and walk or climb with it at full speed.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 210,
        "min_level": 15,
        "level": 15,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, the retriever can pick it up as part of the retriever's move and walk or climb with it at full speed.",
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
        # Add creature-specific abilities
        self.abilities.extend(['faultless_tracker'])

    def faultless_tracker(self) -> str:
        """Faultless Tracker: The retriever is given a quarry by its master. The quarry can be a specific creature or object the m..."""
        return "The retriever is given a quarry by its master. The quarry can be a specific creature or object the master is personally acquainted with, or it can be a general type of creature or object the master ha"

