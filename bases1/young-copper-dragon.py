# bases1/young-copper-dragon.py
"""
YoungCopperDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-copper-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungCopperDragon(GlobalCreatureBaseClass):
    """
    YoungCopperDragon creature
    Size: Large, Type: dragon (Metallic), chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 119,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "dragon (Metallic), chaotic good",
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: ..."""
        return "The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage.Claw. Melee Weapon Attack: +"
    def multiattack(self) -> str:
        """Multiattack: The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: ..."""
        return "The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage.Claw. Melee Weapon Attack: +"

