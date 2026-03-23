# bases1/mammoth.py
"""
Mammoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mammoth
"""
from creature_base import GlobalCreatureBaseClass


class Mammoth(GlobalCreatureBaseClass):
    """
    Mammoth creature
    Size: Huge, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 126,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast, unaligned",
        "hit_points_up": [12, 12, 12],
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
        self.abilities.extend(['trampling_charge'])

    def trampling_charge(self) -> str:
        """Trampling Charge: If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack..."""
        return "If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 18 Strength saving throw or be knocked prone. If"
    def trampling_charge(self) -> str:
        """Trampling Charge: If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack..."""
        return "If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 18 Strength saving throw or be knocked prone. If"

