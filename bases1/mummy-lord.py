# bases1/mummy-lord.py
"""
MummyLord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mummy-lord
"""
from creature_base import GlobalCreatureBaseClass


class MummyLord(GlobalCreatureBaseClass):
    """
    MummyLord creature
    Size: Medium, Type: undead, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 97,
        "min_level": 16,
        "level": 16,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, lawful evil",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The mummy lord has advantage on saving throws against spells and other magical effects.Rejuvenation...."""
        return "The mummy lord has advantage on saving throws against spells and other magical effects.Rejuvenation. A destroyed mummy lord gains a new body in 24 hours if its heart is intact, regaining all its hit p"
    def magic_resistance(self) -> str:
        """Magic Resistance: The mummy lord has advantage on saving throws against spells and other magical effects.Rejuvenation...."""
        return "The mummy lord has advantage on saving throws against spells and other magical effects.Rejuvenation. A destroyed mummy lord gains a new body in 24 hours if its heart is intact, regaining all its hit p"

