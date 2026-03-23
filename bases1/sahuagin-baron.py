# bases1/sahuagin-baron.py
"""
SahuaginBaron creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sahuagin-baron
"""
from creature_base import GlobalCreatureBaseClass


class SahuaginBaron(GlobalCreatureBaseClass):
    """
    SahuaginBaron creature
    Size: Large, Type: humanoid (Sahuagin), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 76,
        "min_level": 6,
        "level": 6,
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
        "type": "humanoid (Sahuagin), lawful evil",
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
        self.abilities.extend(['blood_frenzy'])

    def blood_frenzy(self) -> str:
        """Blood Frenzy: The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit ..."""
        return "The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but he needs to be submerged "
    def blood_frenzy(self) -> str:
        """Blood Frenzy: The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit ..."""
        return "The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but he needs to be submerged "

