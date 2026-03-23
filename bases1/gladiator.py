# bases1/gladiator.py
"""
Gladiator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gladiator
"""
from creature_base import GlobalCreatureBaseClass


class Gladiator(GlobalCreatureBaseClass):
    """
    Gladiator creature
    Size: Medium, Type: or smaller creature, it must succeed on a DC 15 Strength saving throw or be knocked prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 112,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature, it must succeed on a DC 15 Strength saving throw or be knocked prone.",
        "hit_points_up": [11, 11, 11],
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
        self.abilities.extend(['brave'])

    def brave(self) -> str:
        """Brave: The gladiator has advantage on saving throws against being frightened.Brute. A melee weapon deals on..."""
        return "The gladiator has advantage on saving throws against being frightened.Brute. A melee weapon deals one extra die of its damage when the gladiator hits with it (included in the attack).ActionsMultiattac"
    def brave(self) -> str:
        """Brave: The gladiator has advantage on saving throws against being frightened.Brute. A melee weapon deals on..."""
        return "The gladiator has advantage on saving throws against being frightened.Brute. A melee weapon deals one extra die of its damage when the gladiator hits with it (included in the attack).ActionsMultiattac"

