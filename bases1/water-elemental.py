# bases1/water-elemental.py
"""
WaterElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=water-elemental
"""
from creature_base import GlobalCreatureBaseClass


class WaterElemental(GlobalCreatureBaseClass):
    """
    WaterElemental creature
    Size: Large, Type: or smaller, it is also grappled (escape DC 14). Until this grapple ends, the target is restrained and unable to breathe unless it can breathe water. If the saving throw is successful, the target is pushed out of the elemental's space. The elemental can grapple one Large creature or up to two Medium or smaller creatures at one time. At the start of each of the elemental's turns, each target grappled by it takes 13 (2d8 + 4) bludgeoning damage. A creature within 5 feet of the elemental can pull a creature or object out of it by taking an action to make a DC 14 Strength check and succeeding.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 114,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller, it is also grappled (escape DC 14). Until this grapple ends, the target is restrained and unable to breathe unless it can breathe water. If the saving throw is successful, the target is pushed out of the elemental's space. The elemental can grapple one Large creature or up to two Medium or smaller creatures at one time. At the start of each of the elemental's turns, each target grappled by it takes 13 (2d8 + 4) bludgeoning damage. A creature within 5 feet of the elemental can pull a creature or object out of it by taking an action to make a DC 14 Strength check and succeeding.",
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
        self.abilities.extend(['water_form'])

    def water_form(self) -> str:
        """Water Form: The elemental can enter a hostile creature's space and stop there. It can move through a space as na..."""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.Freeze. If the elemental takes cold damage, it partially freez"
    def water_form(self) -> str:
        """Water Form: The elemental can enter a hostile creature's space and stop there. It can move through a space as na..."""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.Freeze. If the elemental takes cold damage, it partially freez"

