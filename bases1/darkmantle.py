# bases1/darkmantle.py
"""
Darkmantle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=darkmantle
"""
from creature_base import GlobalCreatureBaseClass


class Darkmantle(GlobalCreatureBaseClass):
    """
    Darkmantle creature
    Size: Medium, Type: or smaller and the darkmantle has advantage on the attack roll, it attaches by engulfing the target's head, and the target is also blinded and unable to breathe while the darkmantle is attached in this way. While attached to the target, the darkmantle can attack no other creature except the target but has advantage on its attack rolls. The darkmantle's speed also becomes 0, it can't benefit from any bonus to its speed, and it moves with the target. A creature can detach the darkmantle by making a successful DC 13 Strength check as an action. On its turn, the darkmantle can detach itself from the target by using 5 feet of movement.
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
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller and the darkmantle has advantage on the attack roll, it attaches by engulfing the target's head, and the target is also blinded and unable to breathe while the darkmantle is attached in this way. While attached to the target, the darkmantle can attack no other creature except the target but has advantage on its attack rolls. The darkmantle's speed also becomes 0, it can't benefit from any bonus to its speed, and it moves with the target. A creature can detach the darkmantle by making a successful DC 13 Strength check as an action. On its turn, the darkmantle can detach itself from the target by using 5 feet of movement.",
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
        self.abilities.extend(['echolocation'])

    def echolocation(self) -> str:
        """Echolocation: The darkmantle can't use its blindsight while deafened.False Appearance. While the darkmantle remain..."""
        return "The darkmantle can't use its blindsight while deafened.False Appearance. While the darkmantle remains motionless, it is indistinguishable from a cave formation such as a stalactite or stalagmite.Actio"
    def echolocation(self) -> str:
        """Echolocation: The darkmantle can't use its blindsight while deafened.False Appearance. While the darkmantle remain..."""
        return "The darkmantle can't use its blindsight while deafened.False Appearance. While the darkmantle remains motionless, it is indistinguishable from a cave formation such as a stalactite or stalagmite.Actio"

