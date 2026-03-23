# bases1/reef-manta-ray.py
"""
ReefMantaRay creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=reef-manta-ray
"""
from creature_base import GlobalCreatureBaseClass


class ReefMantaRay(GlobalCreatureBaseClass):
    """
    ReefMantaRay creature
    Size: Huge, Type: beast). Her eyes are on the side of her large head and she feeds on plankton.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 16,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast). Her eyes are on the side of her large head and she feeds on plankton.",
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
        # Add creature-specific abilities
        self.abilities.extend(['charge'])

    def charge(self) -> str:
        """Charge: If the manta ray moves at least 20 feet straight toward a target and then hits it with a ram attack ..."""
        return "If the manta ray moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature,"

