# bases1/spirit-naga.py
"""
SpiritNaga creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spirit-naga
"""
from creature_base import GlobalCreatureBaseClass


class SpiritNaga(GlobalCreatureBaseClass):
    """
    SpiritNaga creature
    Size: Large, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 75,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, chaotic evil",
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
        self.abilities.extend(['rejuvenation'])

    def rejuvenation(self) -> str:
        """Rejuvenation: If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell c..."""
        return "If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is a 10th-level spellcaster. Its spell"
    def rejuvenation(self) -> str:
        """Rejuvenation: If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell c..."""
        return "If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is a 10th-level spellcaster. Its spell"

