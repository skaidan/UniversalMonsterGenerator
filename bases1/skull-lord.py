# bases1/skull-lord.py
"""
SkullLord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=skull-lord
"""
from creature_base import GlobalCreatureBaseClass


class SkullLord(GlobalCreatureBaseClass):
    """
    SkullLord creature
    Size: Medium, Type: Undead (Sorcerer), typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 112,
        "min_level": 16,
        "level": 16,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Undead (Sorcerer), typically Lawful Evil",
        "hit_points_up": [11, 11, 11],
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
        self.abilities.extend(['evasion'])

    def evasion(self) -> str:
        """Evasion: If the skull lord is subjected to an effect that allows it to make a Dexterity saving throw to take ..."""
        return "If the skull lord is subjected to an effect that allows it to make a Dexterity saving throw to take only half the damage, the skull lord instead takes no damage if it succeeds on the saving throw and "

