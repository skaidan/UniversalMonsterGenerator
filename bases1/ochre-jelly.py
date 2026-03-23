# bases1/ochre-jelly.py
"""
OchreJelly creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ochre-jelly
"""
from creature_base import GlobalCreatureBaseClass


class OchreJelly(GlobalCreatureBaseClass):
    """
    OchreJelly creature
    Size: Medium, Type: or larger is subjected to lightning or slashing damage, it splits into two new jellies if it has at least 10 hit points. Each new jelly has hit points equal to half the original jelly's, rounded down. New jellies are one size smaller than the original jelly.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 8,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or larger is subjected to lightning or slashing damage, it splits into two new jellies if it has at least 10 hit points. Each new jelly has hit points equal to half the original jelly's, rounded down. New jellies are one size smaller than the original jelly.",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['amorphous'])

    def amorphous(self) -> str:
        """Amorphous: The jelly can move through a space as narrow as 1 inch wide without squeezing.Spider Climb. The jell..."""
        return "The jelly can move through a space as narrow as 1 inch wide without squeezing.Spider Climb. The jelly can climb difficult surfaces, including upside down on ceilings, without needing to make an abilit"
    def amorphous(self) -> str:
        """Amorphous: The jelly can move through a space as narrow as 1 inch wide without squeezing.Spider Climb. The jell..."""
        return "The jelly can move through a space as narrow as 1 inch wide without squeezing.Spider Climb. The jelly can climb difficult surfaces, including upside down on ceilings, without needing to make an abilit"

