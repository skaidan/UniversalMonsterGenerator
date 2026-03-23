# bases1/twig-blight.py
"""
TwigBlight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=twig-blight
"""
from creature_base import GlobalCreatureBaseClass


class TwigBlight(GlobalCreatureBaseClass):
    """
    TwigBlight creature
    Size: Small, Type: plant, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 4,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "plant, neutral evil",
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
        """False Appearance: While the blight remains motionless, it is indistinguishable from a dead shrub.ActionsClaws. Melee W..."""
        return "While the blight remains motionless, it is indistinguishable from a dead shrub.ActionsClaws. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.A twig blight is "
    def false_appearance(self) -> str:
        """False Appearance: While the blight remains motionless, it is indistinguishable from a dead shrub.ActionsClaws. Melee W..."""
        return "While the blight remains motionless, it is indistinguishable from a dead shrub.ActionsClaws. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.A twig blight is "

