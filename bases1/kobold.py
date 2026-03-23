# bases1/kobold.py
"""
Kobold creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kobold
"""
from creature_base import GlobalCreatureBaseClass


class Kobold(GlobalCreatureBaseClass):
    """
    Kobold creature
    Size: Small, Type: humanoid (Kobold), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 5,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "humanoid (Kobold), lawful evil",
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
        self.abilities.extend(['sunlight_sensitivity'])

    def sunlight_sensitivity(self) -> str:
        """Sunlight Sensitivity: While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) ch..."""
        return "While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.Pack Tactics. The kobold has advantage on an attack roll against a creature "
    def sunlight_sensitivity(self) -> str:
        """Sunlight Sensitivity: While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) ch..."""
        return "While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.Pack Tactics. The kobold has advantage on an attack roll against a creature "

