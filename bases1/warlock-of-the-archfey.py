# bases1/warlock-of-the-archfey.py
"""
WarlockOfTheArchfey creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warlock-of-the-archfey
"""
from creature_base import GlobalCreatureBaseClass


class WarlockOfTheArchfey(GlobalCreatureBaseClass):
    """
    WarlockOfTheArchfey creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 67,
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
        "size": "Medium",
        "type": "Humanoid, any alignment",
        "hit_points_up": [6, 6, 6],
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
        """Multiattack: The warlock makes two Rapier attacks, or it uses Bewildering Word twice.Rapier. Melee Weapon Attack:..."""
        return "The warlock makes two Rapier attacks, or it uses Bewildering Word twice.Rapier. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 7 (2d6) force damage.Bewi"

