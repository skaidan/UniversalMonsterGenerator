# bases1/guardian-naga.py
"""
GuardianNaga creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=guardian-naga
"""
from creature_base import GlobalCreatureBaseClass


class GuardianNaga(GlobalCreatureBaseClass):
    """
    GuardianNaga creature
    Size: Large, Type: monstrosity, lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 127,
        "min_level": 11,
        "level": 11,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, lawful good",
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
        self.abilities.extend(['rejuvenation'])

    def rejuvenation(self) -> str:
        """Rejuvenation: If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell c..."""
        return "If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is an 11th-level spellcaster. Its spel"
    def rejuvenation(self) -> str:
        """Rejuvenation: If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell c..."""
        return "If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is an 11th-level spellcaster. Its spel"

