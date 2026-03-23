# bases1/lemure.py
"""
Lemure creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lemure
"""
from creature_base import GlobalCreatureBaseClass


class Lemure(GlobalCreatureBaseClass):
    """
    Lemure creature
    Size: Medium, Type: fiend (Devil), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 7,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fiend (Devil), lawful evil",
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
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the lemure's darkvision.Hellish Rejuvenation. A lemure that dies in ..."""
        return "Magical darkness doesn't impede the lemure's darkvision.Hellish Rejuvenation. A lemure that dies in the Nine Hells comes back to life with all its hit points in 1d10 days unless it is killed by a good"
    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the lemure's darkvision.Hellish Rejuvenation. A lemure that dies in ..."""
        return "Magical darkness doesn't impede the lemure's darkvision.Hellish Rejuvenation. A lemure that dies in the Nine Hells comes back to life with all its hit points in 1d10 days unless it is killed by a good"

