# bases1/brain-in-a-jar.py
"""
BrainInAJar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=brain-in-a-jar
"""
from creature_base import GlobalCreatureBaseClass


class BrainInAJar(GlobalCreatureBaseClass):
    """
    BrainInAJar creature
    Size: Small, Type: undead, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 55,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "undead, any alignment",
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
        self.abilities.extend(['detect_sentience'])

    def detect_sentience(self) -> str:
        """Detect Sentience: The brain can sense the presence and location of any creature within 300 feet of it that has an Inte..."""
        return "The brain can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a m"

