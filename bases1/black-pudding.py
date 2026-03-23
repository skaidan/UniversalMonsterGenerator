# bases1/black-pudding.py
"""
BlackPudding creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=black-pudding
"""
from creature_base import GlobalCreatureBaseClass


class BlackPudding(GlobalCreatureBaseClass):
    """
    BlackPudding creature
    Size: Medium, Type: or larger is subjected to lightning or slashing damage, it splits into two new puddings if it has at least 10 hit points. Each new pudding has hit points equal to half the original pudding's, rounded down. New puddings are one size smaller than the original pudding.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 85,
        "min_level": 5,
        "level": 5,
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
        "type": "or larger is subjected to lightning or slashing damage, it splits into two new puddings if it has at least 10 hit points. Each new pudding has hit points equal to half the original pudding's, rounded down. New puddings are one size smaller than the original pudding.",
        "hit_points_up": [8, 8, 8],
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
        """Amorphous: The pudding can move through a space as narrow as 1 inch wide without squeezing.Corrosive Form. A cr..."""
        return "The pudding can move through a space as narrow as 1 inch wide without squeezing.Corrosive Form. A creature that touches the pudding or hits it with a melee attack while within 5 feet of it takes 4 (1d"
    def amorphous(self) -> str:
        """Amorphous: The pudding can move through a space as narrow as 1 inch wide without squeezing.Corrosive Form. A cr..."""
        return "The pudding can move through a space as narrow as 1 inch wide without squeezing.Corrosive Form. A creature that touches the pudding or hits it with a melee attack while within 5 feet of it takes 4 (1d"

