# bases1/bullywug-knight.py
"""
BullywugKnight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bullywug-knight
"""
from creature_base import GlobalCreatureBaseClass


class BullywugKnight(GlobalCreatureBaseClass):
    """
    BullywugKnight creature
    Size: Medium, Type: humanoid, typically Lawful Good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 66,
        "min_level": 4,
        "level": 4,
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
        "type": "humanoid, typically Lawful Good",
        "hit_points_up": [6, 6, 6],
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The knight can breathe air and water.Speak with Frogs and Toads. The knight can communicate simple c..."""
        return "The knight can breathe air and water.Speak with Frogs and Toads. The knight can communicate simple concepts to frogs and toads when it speaks in Bullywug.Standing Leap. The knight's long jump is up to"

