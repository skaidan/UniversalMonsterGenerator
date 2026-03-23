# bases1/minor-water-elemental.py
"""
MinorWaterElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minor-water-elemental
"""
from creature_base import GlobalCreatureBaseClass


class MinorWaterElemental(GlobalCreatureBaseClass):
    """
    MinorWaterElemental creature
    Size: Small, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 39,
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
        "size": "Small",
        "type": "elemental, neutral",
        "hit_points_up": [3, 3, 3],
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
        self.abilities.extend(['water_form'])

    def water_form(self) -> str:
        """Water Form: The elemental can enter a hostile creature's space and stop there. It can move through a space as na..."""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.Freeze. If the elemental takes cold damage, it partially freez"

