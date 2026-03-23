# bases1/devilroot.py
"""
Devilroot creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=devilroot
"""
from creature_base import GlobalCreatureBaseClass


class Devilroot(GlobalCreatureBaseClass):
    """
    Devilroot creature
    Size: Medium, Type: plant, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 105,
        "min_level": 8,
        "level": 8,
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
        "type": "plant, neutral evil",
        "hit_points_up": [10, 10, 10],
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the devilroot remains motionless, it is indistinguishable from an ordinary plant.Speak With Pl..."""
        return "While the devilroot remains motionless, it is indistinguishable from an ordinary plant.Speak With Plants. The devilroot can communicate with plants and plant creatures as if they shared a language.Act"

