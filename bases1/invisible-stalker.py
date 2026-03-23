# bases1/invisible-stalker.py
"""
InvisibleStalker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=invisible-stalker
"""
from creature_base import GlobalCreatureBaseClass


class InvisibleStalker(GlobalCreatureBaseClass):
    """
    InvisibleStalker creature
    Size: Medium, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 104,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "elemental, neutral",
        "hit_points_up": [10, 10, 10],
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
        self.abilities.extend(['invisibility'])

    def invisibility(self) -> str:
        """Invisibility: The stalker is invisible.Faultless Tracker. The stalker is given a quarry by its summoner. The stalk..."""
        return "The stalker is invisible.Faultless Tracker. The stalker is given a quarry by its summoner. The stalker knows the direction and distance to its quarry as long as the two of them are on the same plane o"
    def invisibility(self) -> str:
        """Invisibility: The stalker is invisible.Faultless Tracker. The stalker is given a quarry by its summoner. The stalk..."""
        return "The stalker is invisible.Faultless Tracker. The stalker is given a quarry by its summoner. The stalker knows the direction and distance to its quarry as long as the two of them are on the same plane o"

