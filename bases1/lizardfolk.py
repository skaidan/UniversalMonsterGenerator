# bases1/lizardfolk.py
"""
Lizardfolk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lizardfolk
"""
from creature_base import GlobalCreatureBaseClass


class Lizardfolk(GlobalCreatureBaseClass):
    """
    Lizardfolk creature
    Size: Medium, Type: humanoid (Lizardfolk), neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Lizardfolk), neutral",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The lizardfolk can hold its breath for 15 minutes.ActionsMultiattack. The lizardfolk makes two melee..."""
        return "The lizardfolk can hold its breath for 15 minutes.ActionsMultiattack. The lizardfolk makes two melee attacks, each one with a different weapon.Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one ta"
    def hold_breath(self) -> str:
        """Hold Breath: The lizardfolk can hold its breath for 15 minutes.ActionsMultiattack. The lizardfolk makes two melee..."""
        return "The lizardfolk can hold its breath for 15 minutes.ActionsMultiattack. The lizardfolk makes two melee attacks, each one with a different weapon.Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one ta"

