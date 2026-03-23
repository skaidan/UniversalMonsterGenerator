# bases1/purple-worm.py
"""
PurpleWorm creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=purple-worm
"""
from creature_base import GlobalCreatureBaseClass


class PurpleWorm(GlobalCreatureBaseClass):
    """
    PurpleWorm creature
    Size: Large, Type: or smaller creature, it must succeed on a DC 19 Dexterity saving throw or be swallowed by the worm. A swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the worm, and it takes 21 (6d6) acid damage at the start of each of the worm's turns. If the worm takes 30 damage or more on a single turn from a creature inside it, the worm must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the worm. If the worm dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 20 feet of movement, exiting prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 247,
        "min_level": 16,
        "level": 16,
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
        "type": "or smaller creature, it must succeed on a DC 19 Dexterity saving throw or be swallowed by the worm. A swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the worm, and it takes 21 (6d6) acid damage at the start of each of the worm's turns. If the worm takes 30 damage or more on a single turn from a creature inside it, the worm must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the worm. If the worm dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 20 feet of movement, exiting prone.",
        "hit_points_up": [24, 24, 24],
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
        self.abilities.extend(['tunneler'])

    def tunneler(self) -> str:
        """Tunneler: The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel..."""
        return "The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel in its wake.ActionsMultiattack. The worm makes two attacks: one with its bite and one with its stin"
    def tunneler(self) -> str:
        """Tunneler: The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel..."""
        return "The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel in its wake.ActionsMultiattack. The worm makes two attacks: one with its bite and one with its stin"

