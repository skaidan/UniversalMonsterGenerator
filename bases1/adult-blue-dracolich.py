# bases1/adult-blue-dracolich.py
"""
AdultBlueDracolich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-blue-dracolich
"""
from creature_base import GlobalCreatureBaseClass


class AdultBlueDracolich(GlobalCreatureBaseClass):
    """
    AdultBlueDracolich creature
    Size: Huge, Type: undead, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 225,
        "min_level": 18,
        "level": 18,
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
        "type": "undead, lawful evil",
        "hit_points_up": [22, 22, 22],
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
        """Legendary Resistance (3/Day): If the dracolich fails a saving throw, it can choose to succeed instead.Magic Resistance. The dracol..."""
        return "If the dracolich fails a saving throw, it can choose to succeed instead.Magic Resistance. The dracolich has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The "
    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the dracolich fails a saving throw, it can choose to succeed instead.Magic Resistance. The dracol..."""
        return "If the dracolich fails a saving throw, it can choose to succeed instead.Magic Resistance. The dracolich has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The "

