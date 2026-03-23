# bases1/girallon.py
"""
Girallon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=girallon
"""
from creature_base import GlobalCreatureBaseClass


class Girallon(GlobalCreatureBaseClass):
    """
    Girallon creature
    Size: Large, Type: Monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 59,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Monstrosity, unaligned",
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The girallon makes one Bite attack and four Claw attacks.Bite. Melee Weapon Attack: +6 to hit, reach..."""
        return "The girallon makes one Bite attack and four Claw attacks.Bite. Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 7 (1d6 + 4) piercing damage.Claw. Melee Weapon Attack: +6 to hit, reach 1"

