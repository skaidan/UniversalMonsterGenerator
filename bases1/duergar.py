# bases1/duergar.py
"""
Duergar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar
"""
from creature_base import GlobalCreatureBaseClass


class Duergar(GlobalCreatureBaseClass):
    """
    Duergar creature
    Size: Medium, Type: humanoid (Dwarf), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 26,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Dwarf), lawful evil",
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
        self.abilities.extend(['duergar_resilience'])

    def duergar_resilience(self) -> str:
        """Duergar Resilience: The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resi..."""
        return "The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage "
    def duergar_resilience(self) -> str:
        """Duergar Resilience: The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resi..."""
        return "The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage "

