# bases1/cloaker.py
"""
Cloaker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cloaker
"""
from creature_base import GlobalCreatureBaseClass


class Cloaker(GlobalCreatureBaseClass):
    """
    Cloaker creature
    Size: Large, Type: or smaller, the cloaker attaches to it. If the cloaker has advantage against the target, the cloaker attaches to the target's head, and the target is blinded and unable to breathe while the cloaker is attached. While attached, the cloaker can make this attack only against the target and has advantage on the attack roll. The cloaker can detach itself by spending 5 feet of its movement. A creature, including the target, can take its action to detach the cloaker by succeeding on a DC 16 Strength check.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 78,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller, the cloaker attaches to it. If the cloaker has advantage against the target, the cloaker attaches to the target's head, and the target is blinded and unable to breathe while the cloaker is attached. While attached, the cloaker can make this attack only against the target and has advantage on the attack roll. The cloaker can detach itself by spending 5 feet of its movement. A creature, including the target, can take its action to detach the cloaker by succeeding on a DC 16 Strength check.",
        "hit_points_up": [7, 7, 7],
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
        self.abilities.extend(['damage_transfer'])

    def damage_transfer(self) -> str:
        """Damage Transfer: While attached to a creature, the cloaker takes only half the damage dealt to it (rounded down), and..."""
        return "While attached to a creature, the cloaker takes only half the damage dealt to it (rounded down), and that creature takes the other half.False Appearance. While the cloaker remains motionless without i"
    def damage_transfer(self) -> str:
        """Damage Transfer: While attached to a creature, the cloaker takes only half the damage dealt to it (rounded down), and..."""
        return "While attached to a creature, the cloaker takes only half the damage dealt to it (rounded down), and that creature takes the other half.False Appearance. While the cloaker remains motionless without i"

