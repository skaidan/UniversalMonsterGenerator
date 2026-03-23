# bases1/juiblex.py
"""
Juiblex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=juiblex
"""
from creature_base import GlobalCreatureBaseClass


class Juiblex(GlobalCreatureBaseClass):
    """
    Juiblex creature
    Size: Huge, Type: Fiend (Demon), Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 350,
        "min_level": 24,
        "level": 24,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Fiend (Demon), Chaotic Evil",
        "hit_points_up": [35, 35, 35],
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
        self.abilities.extend(['foul'])

    def foul(self) -> str:
        """Foul: Any creature other than an Ooze that starts its turn within 10 feet of Juiblex must succeed on a DC ..."""
        return "Any creature other than an Ooze that starts its turn within 10 feet of Juiblex must succeed on a DC 21 Constitution saving throw or be poisoned until the start of the creature's next turn.Legendary Re"

