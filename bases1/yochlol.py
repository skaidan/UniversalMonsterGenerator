# bases1/yochlol.py
"""
Yochlol creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yochlol
"""
from creature_base import GlobalCreatureBaseClass


class Yochlol(GlobalCreatureBaseClass):
    """
    Yochlol creature
    Size: Medium, Type: Fiend (Demon, Shapechanger), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 136,
        "min_level": 11,
        "level": 11,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fiend (Demon, Shapechanger), chaotic evil",
        "hit_points_up": [13, 13, 13],
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
        self.abilities.extend(['shapechanger'])

    def shapechanger(self) -> str:
        """Shapechanger: The yochlol can use its action to polymorph into a form that resembles a female drow or giant spider..."""
        return "The yochlol can use its action to polymorph into a form that resembles a female drow or giant spider, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing "
    def shapechanger(self) -> str:
        """Shapechanger: The yochlol can use its action to polymorph into a form that resembles a female drow or giant spider..."""
        return "The yochlol can use its action to polymorph into a form that resembles a female drow or giant spider, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing "

