# bases1/chuul.py
"""
Chuul creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chuul
"""
from creature_base import GlobalCreatureBaseClass


class Chuul(GlobalCreatureBaseClass):
    """
    Chuul creature
    Size: Large, Type: or smaller creature and the chuul doesn't have two other creatures grappled.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 93,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller creature and the chuul doesn't have two other creatures grappled.",
        "hit_points_up": [9, 9, 9],
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
        """Amphibious: The chuul can breathe air and water.Sense Magic. The chuul senses magic within 120 feet of it at wil..."""
        return "The chuul can breathe air and water.Sense Magic. The chuul senses magic within 120 feet of it at will. This trait otherwise works like the detect magic spell but isn't itself magical.ActionsMultiattac"
    def amphibious(self) -> str:
        """Amphibious: The chuul can breathe air and water.Sense Magic. The chuul senses magic within 120 feet of it at wil..."""
        return "The chuul can breathe air and water.Sense Magic. The chuul senses magic within 120 feet of it at will. This trait otherwise works like the detect magic spell but isn't itself magical.ActionsMultiattac"

