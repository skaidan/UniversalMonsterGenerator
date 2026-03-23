# bases1/warlock-of-the-great-old-one.py
"""
WarlockOfTheGreatOldOne creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warlock-of-the-great-old-one
"""
from creature_base import GlobalCreatureBaseClass


class WarlockOfTheGreatOldOne(GlobalCreatureBaseClass):
    """
    WarlockOfTheGreatOldOne creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 91,
        "min_level": 7,
        "level": 7,
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
        "hit_points_up": [9, 9, 9],
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
        self.abilities.extend(['whispering_aura'])

    def whispering_aura(self) -> str:
        """Whispering Aura: At the start of each of the warlock's turns, each creature of its choice within 10 feet of it must s..."""
        return "At the start of each of the warlock's turns, each creature of its choice within 10 feet of it must succeed on a DC 15 Wisdom saving throw or take 10 (3d6) psychic damage, provided that the warlock isn"

