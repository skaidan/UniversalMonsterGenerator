# bases1/death-tyrant.py
"""
DeathTyrant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-tyrant
"""
from creature_base import GlobalCreatureBaseClass


class DeathTyrant(GlobalCreatureBaseClass):
    """
    DeathTyrant creature
    Size: Large, Type: or smaller nonmagical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger object or creation of magical force, this ray disintegrates a 10-foot cube of it.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 187,
        "min_level": 15,
        "level": 15,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller nonmagical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger object or creation of magical force, this ray disintegrates a 10-foot cube of it.",
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
        self.abilities.extend(['negative_energy_cone'])

    def negative_energy_cone(self) -> str:
        """Negative Energy Cone: The death tyrant's central eye emits an invisible, magical 1 50-foot cone of negative energy. At the..."""
        return "The death tyrant's central eye emits an invisible, magical 1 50-foot cone of negative energy. At the start of each of its turns, the tyrant decides which way the cone faces and whether the cone is act"
    def negative_energy_cone(self) -> str:
        """Negative Energy Cone: The death tyrant's central eye emits an invisible, magical 1 50-foot cone of negative energy. At the..."""
        return "The death tyrant's central eye emits an invisible, magical 1 50-foot cone of negative energy. At the start of each of its turns, the tyrant decides which way the cone faces and whether the cone is act"

