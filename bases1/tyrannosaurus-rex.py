# bases1/tyrannosaurus-rex.py
"""
TyrannosaurusRex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tyrannosaurus-rex
"""
from creature_base import GlobalCreatureBaseClass


class TyrannosaurusRex(GlobalCreatureBaseClass):
    """
    TyrannosaurusRex creature
    Size: Medium, Type: or smaller creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the tyrannosaurus can't bite another target.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 136,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the tyrannosaurus can't bite another target.",
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both att..."""
        return "The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both attacks against the same target.Bite. Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 3"
    def multiattack(self) -> str:
        """Multiattack: The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both att..."""
        return "The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both attacks against the same target.Bite. Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 3"

