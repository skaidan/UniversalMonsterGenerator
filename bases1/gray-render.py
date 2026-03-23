# bases1/gray-render.py
"""
GrayRender creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gray-render
"""
from creature_base import GlobalCreatureBaseClass


class GrayRender(GlobalCreatureBaseClass):
    """
    GrayRender creature
    Size: Medium, Type: or smaller, the target must succeed on a DC 16 Strength saving throw or be knocked prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 189,
        "min_level": 13,
        "level": 13,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, the target must succeed on a DC 16 Strength saving throw or be knocked prone.",
        "hit_points_up": [18, 18, 18],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The gray render makes one Bite attack and two Claw attacks.Bite. Melee Weapon Attack: +8 to hit, rea..."""
        return "The gray render makes one Bite attack and two Claw attacks.Bite. Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 17 (2d12 + 4) piercing damage. If the target is Medium or smaller, the ta"

