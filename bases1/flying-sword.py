# bases1/flying-sword.py
"""
FlyingSword creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flying-sword
"""
from creature_base import GlobalCreatureBaseClass


class FlyingSword(GlobalCreatureBaseClass):
    """
    FlyingSword creature
    Size: Small, Type: construct, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 17,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "construct, unaligned",
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
        self.abilities.extend(['antimagic_susceptibility'])

    def antimagic_susceptibility(self) -> str:
        """Antimagic Susceptibility: The sword is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the..."""
        return "The sword is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the sword must succeed on a Constitution saving throw against the caster's spell save DC or fall uncons"
    def antimagic_susceptibility(self) -> str:
        """Antimagic Susceptibility: The sword is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the..."""
        return "The sword is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the sword must succeed on a Constitution saving throw against the caster's spell save DC or fall uncons"

