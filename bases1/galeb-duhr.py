# bases1/galeb-duhr.py
"""
GalebDuhr creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=galeb-duhr
"""
from creature_base import GlobalCreatureBaseClass


class GalebDuhr(GlobalCreatureBaseClass):
    """
    GalebDuhr creature
    Size: Medium, Type: elemental, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 85,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "elemental, neutral",
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the galeb duhr remains motionless, it is indistinguishable from a normal boulder.Rolling Charg..."""
        return "While the galeb duhr remains motionless, it is indistinguishable from a normal boulder.Rolling Charge. If the galeb duhr rolls at least 20 feet straight toward a target and then hits it with a slam at"
    def false_appearance(self) -> str:
        """False Appearance: While the galeb duhr remains motionless, it is indistinguishable from a normal boulder.Rolling Charg..."""
        return "While the galeb duhr remains motionless, it is indistinguishable from a normal boulder.Rolling Charge. If the galeb duhr rolls at least 20 feet straight toward a target and then hits it with a slam at"

