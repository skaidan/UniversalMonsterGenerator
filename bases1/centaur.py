# bases1/centaur.py
"""
Centaur creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=centaur
"""
from creature_base import GlobalCreatureBaseClass


class Centaur(GlobalCreatureBaseClass):
    """
    Centaur creature
    Size: Large, Type: monstrosity, neutral good
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
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, neutral good",
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
        self.abilities.extend(['charge'])

    def charge(self) -> str:
        """Charge: If the centaur moves at least 30 feet straight toward a target and then hits it with a pike attack o..."""
        return "If the centaur moves at least 30 feet straight toward a target and then hits it with a pike attack on the same turn, the target takes an extra 10 (3d6) piercing damage.ActionsMultiattack. The centaur "
    def charge(self) -> str:
        """Charge: If the centaur moves at least 30 feet straight toward a target and then hits it with a pike attack o..."""
        return "If the centaur moves at least 30 feet straight toward a target and then hits it with a pike attack on the same turn, the target takes an extra 10 (3d6) piercing damage.ActionsMultiattack. The centaur "

