# bases1/bullywug.py
"""
Bullywug creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bullywug
"""
from creature_base import GlobalCreatureBaseClass


class Bullywug(GlobalCreatureBaseClass):
    """
    Bullywug creature
    Size: Medium, Type: humanoid (Bullywug), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Bullywug), neutral evil",
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The bullywug can breathe air and water.Speak with Frogs and Toads. The bullywug can communicate simp..."""
        return "The bullywug can breathe air and water.Speak with Frogs and Toads. The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug.Swamp Camouflage. The bullywug has advanta"
    def amphibious(self) -> str:
        """Amphibious: The bullywug can breathe air and water.Speak with Frogs and Toads. The bullywug can communicate simp..."""
        return "The bullywug can breathe air and water.Speak with Frogs and Toads. The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug.Swamp Camouflage. The bullywug has advanta"

