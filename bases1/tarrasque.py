# bases1/tarrasque.py
"""
Tarrasque creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tarrasque
"""
from creature_base import GlobalCreatureBaseClass


class Tarrasque(GlobalCreatureBaseClass):
    """
    Tarrasque creature
    Size: Large, Type: or smaller creature it is grappling. If the attack hits, the target takes the bite's damage, the target is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the tarrasque, and it takes bO (I6d6) acid damage at the start of each of the tarrasque's turns. If the tarrasque takes 60 damage or more on a single turn from a creature inside it, the tarrasque must succeed on a DC 30 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the tarrasque. If the tarrasque dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 30 feet of movement, exiting prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 676,
        "min_level": 31,
        "level": 31,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 25,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller creature it is grappling. If the attack hits, the target takes the bite's damage, the target is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the tarrasque, and it takes bO (I6d6) acid damage at the start of each of the tarrasque's turns. If the tarrasque takes 60 damage or more on a single turn from a creature inside it, the tarrasque must succeed on a DC 30 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the tarrasque. If the tarrasque dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 30 feet of movement, exiting prone.",
        "hit_points_up": [67, 67, 67],
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
        self.abilities.extend(['legendary_resistance_day'])

    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the tarrasque fails a saving throw, it can choose to succeed instead.Magic Resistance. The tarras..."""
        return "If the tarrasque fails a saving throw, it can choose to succeed instead.Magic Resistance. The tarrasque has advantage on saving throws against spells and other magical effects.Reflective Carapace. Any"
    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the tarrasque fails a saving throw, it can choose to succeed instead.Magic Resistance. The tarras..."""
        return "If the tarrasque fails a saving throw, it can choose to succeed instead.Magic Resistance. The tarrasque has advantage on saving throws against spells and other magical effects.Reflective Carapace. Any"

