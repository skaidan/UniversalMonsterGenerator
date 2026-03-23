# bases1/darkling.py
"""
Darkling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=darkling
"""
from creature_base import GlobalCreatureBaseClass


class Darkling(GlobalCreatureBaseClass):
    """
    Darkling creature
    Size: Small, Type: Fey, typically Chaotic Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "Fey, typically Chaotic Neutral",
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
        self.abilities.extend(['death_flash'])

    def death_flash(self) -> str:
        """Death Flash: When the darkling dies, nonmagical light flashes out from it in a 10-foot radius as its body and pos..."""
        return "When the darkling dies, nonmagical light flashes out from it in a 10-foot radius as its body and possessions, other than metal or magic objects, burn to ash. Any creature in that area must succeed on "

