# bases1/ancient-copper-dragon.py
"""
AncientCopperDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-copper-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientCopperDragon(GlobalCreatureBaseClass):
    """
    AncientCopperDragon creature
    Size: Gargantuan, Type: dragon (Metallic), chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 350,
        "min_level": 22,
        "level": 22,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 21,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "dragon (Metallic), chaotic good",
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
        self.abilities.extend(['legendary_resistance_day'])

    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon ..."""
        return "If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claw"
    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon ..."""
        return "If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claw"

