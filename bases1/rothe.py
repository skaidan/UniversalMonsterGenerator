# bases1/rothe.py
"""
Rothe creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rothe
"""
from creature_base import GlobalCreatureBaseClass


class Rothe(GlobalCreatureBaseClass):
    """
    Rothe creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 15,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
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
        # Add creature-specific abilities
        self.abilities.extend(['charge'])

    def charge(self) -> str:
        """Charge: If the rothé moves at least 20 feet straight toward a target and then hits it with a gore attack on ..."""
        return "If the rothé moves at least 20 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 7 (2d6) piercing damage.ActionsGore. Melee Weapon Attack: +"

