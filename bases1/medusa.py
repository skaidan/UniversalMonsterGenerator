# bases1/medusa.py
"""
Medusa creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=medusa
"""
from creature_base import GlobalCreatureBaseClass


class Medusa(GlobalCreatureBaseClass):
    """
    Medusa creature
    Size: Medium, Type: monstrosity, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 127,
        "min_level": 7,
        "level": 7,
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
        "type": "monstrosity, lawful evil",
        "hit_points_up": [12, 12, 12],
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
        self.abilities.extend(['petrifying_gaze'])

    def petrifying_gaze(self) -> str:
        """Petrifying Gaze: When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the med..."""
        return "When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the medusa can force it to make a DC 14 Constitution saving throw if the medusa isn't incapacitated and can"
    def petrifying_gaze(self) -> str:
        """Petrifying Gaze: When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the med..."""
        return "When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the medusa can force it to make a DC 14 Constitution saving throw if the medusa isn't incapacitated and can"

