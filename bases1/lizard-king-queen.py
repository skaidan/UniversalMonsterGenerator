# bases1/lizard-king-queen.py
"""
LizardKingQueen creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lizard-king-queen
"""
from creature_base import GlobalCreatureBaseClass


class LizardKingQueen(GlobalCreatureBaseClass):
    """
    LizardKingQueen creature
    Size: Medium, Type: humanoid (Lizardfolk), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 78,
        "min_level": 5,
        "level": 5,
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
        "type": "humanoid (Lizardfolk), chaotic evil",
        "hit_points_up": [7, 7, 7],
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The lizardfolk can hold its breath for 15 minutes.Skewer. Once per turn, when the lizardfolk makes a..."""
        return "The lizardfolk can hold its breath for 15 minutes.Skewer. Once per turn, when the lizardfolk makes a melee attack with its trident and hits, the target takes an extra 10 (3d6) damage, and the lizardfo"
    def hold_breath(self) -> str:
        """Hold Breath: The lizardfolk can hold its breath for 15 minutes.Skewer. Once per turn, when the lizardfolk makes a..."""
        return "The lizardfolk can hold its breath for 15 minutes.Skewer. Once per turn, when the lizardfolk makes a melee attack with its trident and hits, the target takes an extra 10 (3d6) damage, and the lizardfo"

