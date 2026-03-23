# bases1/giant-frog.py
"""
GiantFrog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-frog
"""
from creature_base import GlobalCreatureBaseClass


class GiantFrog(GlobalCreatureBaseClass):
    """
    GiantFrog creature
    Size: Small, Type: or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the frog, and it takes 5 (2d4) acid damage at the start of each of the frog's turns. The frog can have only one target swallowed at a time. If the frog dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 18,
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
        "size": "Small",
        "type": "or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the frog, and it takes 5 (2d4) acid damage at the start of each of the frog's turns. The frog can have only one target swallowed at a time. If the frog dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone.",
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The frog can breathe air and water.Standing Leap. The frog's long jump is up to 20 feet and its high..."""
        return "The frog can breathe air and water.Standing Leap. The frog's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start.ActionsBite. Melee Weapon Attack: +3 to hit,"
    def amphibious(self) -> str:
        """Amphibious: The frog can breathe air and water.Standing Leap. The frog's long jump is up to 20 feet and its high..."""
        return "The frog can breathe air and water.Standing Leap. The frog's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start.ActionsBite. Melee Weapon Attack: +3 to hit,"

