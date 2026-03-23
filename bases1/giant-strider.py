# bases1/giant-strider.py
"""
GiantStrider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-strider
"""
from creature_base import GlobalCreatureBaseClass


class GiantStrider(GlobalCreatureBaseClass):
    """
    GiantStrider creature
    Size: Large, Type: Elemental, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
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
        "type": "Elemental, unaligned",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['fire_absorption'])

    def fire_absorption(self) -> str:
        """Fire Absorption: Whenever the giant strider is subjected to fire damage, it takes no damage and regains a number of h..."""
        return "Whenever the giant strider is subjected to fire damage, it takes no damage and regains a number of hit points equal to half the fire damage dealt.ActionsBite. Melee Weapon Attack: +6 to hit, reach 5 f"

