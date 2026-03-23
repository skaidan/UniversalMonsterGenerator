# bases1/pegasus.py
"""
Pegasus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pegasus
"""
from creature_base import GlobalCreatureBaseClass


class Pegasus(GlobalCreatureBaseClass):
    """
    Pegasus creature
    Size: Large, Type: celestial, chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 59,
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
        "size": "Large",
        "type": "celestial, chaotic good",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['hooves'])

    def hooves(self) -> str:
        """Hooves: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.The wh..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.The white winged horses known as pegasi soar through the skies, a vision of grace and majesty.Monster Manu"
    def hooves(self) -> str:
        """Hooves: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.The wh..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.The white winged horses known as pegasi soar through the skies, a vision of grace and majesty.Monster Manu"

