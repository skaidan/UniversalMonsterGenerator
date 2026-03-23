# bases1/adult-silver-dragon.py
"""
AdultSilverDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-silver-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultSilverDragon(GlobalCreatureBaseClass):
    """
    AdultSilverDragon creature
    Size: Huge, Type: dragon (Metallic), lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 243,
        "min_level": 17,
        "level": 17,
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
        "type": "dragon (Metallic), lawful good",
        "hit_points_up": [24, 24, 24],
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
        """Legendary Resistance (3/Day): If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon ..."""
        return "If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claw"
    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon ..."""
        return "If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claw"

