# bases1/rug-of-smothering.py
"""
RugOfSmothering creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rug-of-smothering
"""
from creature_base import GlobalCreatureBaseClass


class RugOfSmothering(GlobalCreatureBaseClass):
    """
    RugOfSmothering creature
    Size: Medium, Type: or smaller creature.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature.",
        "hit_points_up": [3, 3, 3],
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
        self.abilities.extend(['antimagic_susceptibility'])

    def antimagic_susceptibility(self) -> str:
        """Antimagic Susceptibility: The rug is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the r..."""
        return "The rug is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the rug must succeed on a Constitution saving throw against the caster's spell save DC or fall unconsciou"
    def antimagic_susceptibility(self) -> str:
        """Antimagic Susceptibility: The rug is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the r..."""
        return "The rug is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the rug must succeed on a Constitution saving throw against the caster's spell save DC or fall unconsciou"

