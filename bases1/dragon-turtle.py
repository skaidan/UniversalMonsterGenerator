# bases1/dragon-turtle.py
"""
DragonTurtle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragon-turtle
"""
from creature_base import GlobalCreatureBaseClass


class DragonTurtle(GlobalCreatureBaseClass):
    """
    DragonTurtle creature
    Size: Gargantuan, Type: dragon, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 341,
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
        "size": "Gargantuan",
        "type": "dragon, neutral",
        "hit_points_up": [34, 34, 34],
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The dragon turtle can breathe air and water.ActionsMultiattack. The dragon turtle makes three attack..."""
        return "The dragon turtle can breathe air and water.ActionsMultiattack. The dragon turtle makes three attacks: one with its bite and two with its claws. It can make one tail attack in place of its two claw at"
    def amphibious(self) -> str:
        """Amphibious: The dragon turtle can breathe air and water.ActionsMultiattack. The dragon turtle makes three attack..."""
        return "The dragon turtle can breathe air and water.ActionsMultiattack. The dragon turtle makes three attacks: one with its bite and two with its claws. It can make one tail attack in place of its two claw at"

