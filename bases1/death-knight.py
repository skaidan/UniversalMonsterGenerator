# bases1/death-knight.py
"""
DeathKnight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-knight
"""
from creature_base import GlobalCreatureBaseClass


class DeathKnight(GlobalCreatureBaseClass):
    """
    DeathKnight creature
    Size: Medium, Type: undead, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 180,
        "min_level": 18,
        "level": 18,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, chaotic evil",
        "hit_points_up": [18, 18, 18],
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The death knight has advantage on saving throws against spells and other magical effects.Marshal Und..."""
        return "The death knight has advantage on saving throws against spells and other magical effects.Marshal Undead. Unless the death knight is incapacitated, it and undead creatures of its choice within 60 feet "
    def magic_resistance(self) -> str:
        """Magic Resistance: The death knight has advantage on saving throws against spells and other magical effects.Marshal Und..."""
        return "The death knight has advantage on saving throws against spells and other magical effects.Marshal Undead. Unless the death knight is incapacitated, it and undead creatures of its choice within 60 feet "

