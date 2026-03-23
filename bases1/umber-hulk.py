# bases1/umber-hulk.py
"""
UmberHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=umber-hulk
"""
from creature_base import GlobalCreatureBaseClass


class UmberHulk(GlobalCreatureBaseClass):
    """
    UmberHulk creature
    Size: Large, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 93,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, chaotic evil",
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
        self.abilities.extend(['confusing_caze'])

    def confusing_caze(self) -> str:
        """Confusing Caze: When a creature starts its turn within 30 feet of the umber hulk and is able to see the umber hulk's..."""
        return "When a creature starts its turn within 30 feet of the umber hulk and is able to see the umber hulk's eyes, the umber hulk can magically force it to make a DC 15 Charisma saving throw, unless the umber"
    def confusing_caze(self) -> str:
        """Confusing Caze: When a creature starts its turn within 30 feet of the umber hulk and is able to see the umber hulk's..."""
        return "When a creature starts its turn within 30 feet of the umber hulk and is able to see the umber hulk's eyes, the umber hulk can magically force it to make a DC 15 Charisma saving throw, unless the umber"

