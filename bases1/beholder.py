# bases1/beholder.py
"""
Beholder creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=beholder
"""
from creature_base import GlobalCreatureBaseClass


class Beholder(GlobalCreatureBaseClass):
    """
    Beholder creature
    Size: Large, Type: or smaller non magical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger object or creation of magical force, this ray disintegrates a 10-foot cube of it.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 180,
        "min_level": 14,
        "level": 14,
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
        "type": "or smaller non magical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger object or creation of magical force, this ray disintegrates a 10-foot cube of it.",
        "hit_points_up": [18, 18, 18],
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
        self.abilities.extend(['antimagic_cone'])

    def antimagic_cone(self) -> str:
        """Antimagic Cone: The beholder's central eye creates an area of antimagic, as in the antimagic field spell, in a 150-f..."""
        return "The beholder's central eye creates an area of antimagic, as in the antimagic field spell, in a 150-foot cone. At the start of each of its turns, the beholder decides which way the cone faces and wheth"
    def antimagic_cone(self) -> str:
        """Antimagic Cone: The beholder's central eye creates an area of antimagic, as in the antimagic field spell, in a 150-f..."""
        return "The beholder's central eye creates an area of antimagic, as in the antimagic field spell, in a 150-foot cone. At the start of each of its turns, the beholder decides which way the cone faces and wheth"

