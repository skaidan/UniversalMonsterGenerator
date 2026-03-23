# bases1/lich.py
"""
Lich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lich
"""
from creature_base import GlobalCreatureBaseClass


class Lich(GlobalCreatureBaseClass):
    """
    Lich creature
    Size: Medium, Type: undead, any evil alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 135,
        "min_level": 22,
        "level": 22,
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
        "type": "undead, any evil alignment",
        "hit_points_up": [13, 13, 13],
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
        self.abilities.extend(['legendary_resistance_day'])

    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the lich fails a saving throw, it can choose to succeed instead.Rejuvenation. If it has a phylact..."""
        return "If the lich fails a saving throw, it can choose to succeed instead.Rejuvenation. If it has a phylactery, a destroyed lich gains a new body in 1d10 days, regaining all its hit points and becoming activ"
    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the lich fails a saving throw, it can choose to succeed instead.Rejuvenation. If it has a phylact..."""
        return "If the lich fails a saving throw, it can choose to succeed instead.Rejuvenation. If it has a phylactery, a destroyed lich gains a new body in 1d10 days, regaining all its hit points and becoming activ"

