# bases1/young-gold-dragon.py
"""
YoungGoldDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-gold-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungGoldDragon(GlobalCreatureBaseClass):
    """
    YoungGoldDragon creature
    Size: Large, Type: dragon (Metallic), lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 178,
        "min_level": 11,
        "level": 11,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "dragon (Metallic), lawful good",
        "hit_points_up": [17, 17, 17],
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
        """Amphibious: The dragon can breathe air and water.ActionsMultiattack. The dragon makes three attacks: one with it..."""
        return "The dragon can breathe air and water.ActionsMultiattack. The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: "
    def amphibious(self) -> str:
        """Amphibious: The dragon can breathe air and water.ActionsMultiattack. The dragon makes three attacks: one with it..."""
        return "The dragon can breathe air and water.ActionsMultiattack. The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: "

