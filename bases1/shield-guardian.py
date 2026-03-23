# bases1/shield-guardian.py
"""
ShieldGuardian creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shield-guardian
"""
from creature_base import GlobalCreatureBaseClass


class ShieldGuardian(GlobalCreatureBaseClass):
    """
    ShieldGuardian creature
    Size: Large, Type: construct, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 142,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "construct, unaligned",
        "hit_points_up": [14, 14, 14],
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
        self.abilities.extend(['bound'])

    def bound(self) -> str:
        """Bound: The shield guardian is magically bound to an amulet. As long as the guardian and its amulet are on t..."""
        return "The shield guardian is magically bound to an amulet. As long as the guardian and its amulet are on the same plane of existence, the amulet's wearer can telepathically call the guardian to travel to it"
    def bound(self) -> str:
        """Bound: The shield guardian is magically bound to an amulet. As long as the guardian and its amulet are on t..."""
        return "The shield guardian is magically bound to an amulet. As long as the guardian and its amulet are on the same plane of existence, the amulet's wearer can telepathically call the guardian to travel to it"

