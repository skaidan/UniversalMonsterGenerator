# bases1/balor.py
"""
Balor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=balor
"""
from creature_base import GlobalCreatureBaseClass


class Balor(GlobalCreatureBaseClass):
    """
    Balor creature
    Size: Huge, Type: fiend (Demon), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 262,
        "min_level": 20,
        "level": 20,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "fiend (Demon), chaotic evil",
        "hit_points_up": [26, 26, 26],
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
        self.abilities.extend(['death_throes'])

    def death_throes(self) -> str:
        """Death Throes: When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity..."""
        return "When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successful"
    def death_throes(self) -> str:
        """Death Throes: When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity..."""
        return "When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successful"

