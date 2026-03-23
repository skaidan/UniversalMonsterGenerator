# bases1/homunculus.py
"""
Homunculus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=homunculus
"""
from creature_base import GlobalCreatureBaseClass


class Homunculus(GlobalCreatureBaseClass):
    """
    Homunculus creature
    Size: Tiny, Type: construct, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 5,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "construct, neutral",
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
        self.abilities.extend(['telepathic_bond'])

    def telepathic_bond(self) -> str:
        """Telepathic Bond: While the homunculus is on the same plane of existence as its master, it can magically convey what i..."""
        return "While the homunculus is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically.ActionsBite. Melee Weapon Attack:"
    def telepathic_bond(self) -> str:
        """Telepathic Bond: While the homunculus is on the same plane of existence as its master, it can magically convey what i..."""
        return "While the homunculus is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically.ActionsBite. Melee Weapon Attack:"

