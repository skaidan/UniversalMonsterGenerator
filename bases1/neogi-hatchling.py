# bases1/neogi-hatchling.py
"""
NeogiHatchling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=neogi-hatchling
"""
from creature_base import GlobalCreatureBaseClass


class NeogiHatchling(GlobalCreatureBaseClass):
    """
    NeogiHatchling creature
    Size: Tiny, Type: Aberration, typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 7,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "Aberration, typically Lawful Evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['mental_fortitude'])

    def mental_fortitude(self) -> str:
        """Mental Fortitude: The neogi has advantage on saving throws against being charmed or frightened, and magic can't put th..."""
        return "The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Climb. The neogi can climb difficult surfaces, including upside down on ceil"

