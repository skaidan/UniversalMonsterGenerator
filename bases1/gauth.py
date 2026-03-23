# bases1/gauth.py
"""
Gauth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gauth
"""
from creature_base import GlobalCreatureBaseClass


class Gauth(GlobalCreatureBaseClass):
    """
    Gauth creature
    Size: Medium, Type: Aberration (Beholder), typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Aberration (Beholder), typically Lawful Evil",
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
        self.abilities.extend(['death_throes'])

    def death_throes(self) -> str:
        """Death Throes: When the gauth dies, the magical energy within it explodes, and each creature within 10 feet of it m..."""
        return "When the gauth dies, the magical energy within it explodes, and each creature within 10 feet of it must make a DC 14 Dexterity saving throw, taking 13 (3d8) force damage on a failed save, or half as m"

