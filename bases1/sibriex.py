# bases1/sibriex.py
"""
Sibriex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sibriex
"""
from creature_base import GlobalCreatureBaseClass


class Sibriex(GlobalCreatureBaseClass):
    """
    Sibriex creature
    Size: Huge, Type: Fiend (Demon), typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 150,
        "min_level": 19,
        "level": 19,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Fiend (Demon), typically Chaotic Evil",
        "hit_points_up": [15, 15, 15],
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
        self.abilities.extend(['contamination'])

    def contamination(self) -> str:
        """Contamination: The sibriex emits an aura of corruption 30 feet in every direction. Vegetation withers in the aura, ..."""
        return "The sibriex emits an aura of corruption 30 feet in every direction. Vegetation withers in the aura, and the ground in the aura is difficult terrain for other creatures. Any creature that starts its tu"

