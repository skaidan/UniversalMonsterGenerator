# bases1/yeth-hound.py
"""
YethHound creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yeth-hound
"""
from creature_base import GlobalCreatureBaseClass


class YethHound(GlobalCreatureBaseClass):
    """
    YethHound creature
    Size: Large, Type: Fey, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 51,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Fey, typically Neutral Evil",
        "hit_points_up": [5, 5, 5],
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
        # Add creature-specific abilities
        self.abilities.extend(['sunlight_banishment'])

    def sunlight_banishment(self) -> str:
        """Sunlight Banishment: If the yeth hound starts its turn in sunlight, it is transported to the Ethereal Plane. While sunlig..."""
        return "If the yeth hound starts its turn in sunlight, it is transported to the Ethereal Plane. While sunlight shines on the spot from which it vanished, the hound must remain in the Deep Ethereal. After suns"

