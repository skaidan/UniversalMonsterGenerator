# bases1/awakened-shrub.py
"""
AwakenedShrub creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=awakened-shrub
"""
from creature_base import GlobalCreatureBaseClass


class AwakenedShrub(GlobalCreatureBaseClass):
    """
    AwakenedShrub creature
    Size: Small, Type: plant, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 10,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 9,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "plant, unaligned",
        "hit_points_up": [1, 1, 1],
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
        """False Appearance: While the shrub remains motionless, it is indistinguishable from a normal shrub.ActionsRake. Melee W..."""
        return "While the shrub remains motionless, it is indistinguishable from a normal shrub.ActionsRake. Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) slashing damage.An awakened shrub"
    def false_appearance(self) -> str:
        """False Appearance: While the shrub remains motionless, it is indistinguishable from a normal shrub.ActionsRake. Melee W..."""
        return "While the shrub remains motionless, it is indistinguishable from a normal shrub.ActionsRake. Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) slashing damage.An awakened shrub"

