# bases1/air-elemental.py
"""
AirElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=air-elemental
"""
from creature_base import GlobalCreatureBaseClass


class AirElemental(GlobalCreatureBaseClass):
    """
    AirElemental creature
    Size: Large, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 90,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "elemental, neutral",
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
        self.abilities.extend(['air_form'])

    def air_form(self) -> str:
        """Air Form: The elemental can enter a hostile creature's space and stop there. It can move through a space as na..."""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.ActionsMultiattack. The elemental makes two slam attacks.Slam."
    def air_form(self) -> str:
        """Air Form: The elemental can enter a hostile creature's space and stop there. It can move through a space as na..."""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.ActionsMultiattack. The elemental makes two slam attacks.Slam."

