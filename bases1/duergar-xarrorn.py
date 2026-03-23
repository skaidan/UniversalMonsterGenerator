# bases1/duergar-xarrorn.py
"""
DuergarXarrorn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-xarrorn
"""
from creature_base import GlobalCreatureBaseClass


class DuergarXarrorn(GlobalCreatureBaseClass):
    """
    DuergarXarrorn creature
    Size: Medium, Type: Humanoid (Dwarf), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 26,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid (Dwarf), any alignment",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['duergar_resilience'])

    def duergar_resilience(self) -> str:
        """Duergar Resilience: The duergar has advantage on saving throws against spells and the charmed, paralyzed, and poisoned c..."""
        return "The duergar has advantage on saving throws against spells and the charmed, paralyzed, and poisoned conditions.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage on attack rolls, as "

