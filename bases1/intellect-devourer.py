# bases1/intellect-devourer.py
"""
IntellectDevourer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=intellect-devourer
"""
from creature_base import GlobalCreatureBaseClass


class IntellectDevourer(GlobalCreatureBaseClass):
    """
    IntellectDevourer creature
    Size: Tiny, Type: aberration, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 21,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "aberration, lawful evil",
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
        self.abilities.extend(['detect_sentience'])

    def detect_sentience(self) -> str:
        """Detect Sentience: The intellect devourer can sense the presence and location of any creature within 300 feet of it tha..."""
        return "The intellect devourer can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is pro"
    def detect_sentience(self) -> str:
        """Detect Sentience: The intellect devourer can sense the presence and location of any creature within 300 feet of it tha..."""
        return "The intellect devourer can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is pro"

