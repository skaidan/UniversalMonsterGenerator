# bases1/young-silver-dragon.py
"""
YoungSilverDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-silver-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungSilverDragon(GlobalCreatureBaseClass):
    """
    YoungSilverDragon creature
    Size: Large, Type: dragon (Metallic), lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 168,
        "min_level": 10,
        "level": 10,
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
        "hit_points_up": [16, 16, 16],
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
        return "The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage.Claw. Melee Weapon Attack: "
    def multiattack(self) -> str:
        """Multiattack: The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: ..."""
        return "The dragon makes three attacks: one with its bite and two with its claws.Bite. Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage.Claw. Melee Weapon Attack: "

