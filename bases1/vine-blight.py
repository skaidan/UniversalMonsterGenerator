# bases1/vine-blight.py
"""
VineBlight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vine-blight
"""
from creature_base import GlobalCreatureBaseClass


class VineBlight(GlobalCreatureBaseClass):
    """
    VineBlight creature
    Size: Large, Type: or smaller target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the blight can't constrict another target.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 26,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the blight can't constrict another target.",
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the blight remains motionless, it is indistinguishable from a tangle of vines.ActionsConstrict..."""
        return "While the blight remains motionless, it is indistinguishable from a tangle of vines.ActionsConstrict. Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage, and"
    def false_appearance(self) -> str:
        """False Appearance: While the blight remains motionless, it is indistinguishable from a tangle of vines.ActionsConstrict..."""
        return "While the blight remains motionless, it is indistinguishable from a tangle of vines.ActionsConstrict. Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage, and"

