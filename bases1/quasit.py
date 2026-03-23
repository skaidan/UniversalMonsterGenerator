# bases1/quasit.py
"""
Quasit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quasit
"""
from creature_base import GlobalCreatureBaseClass


class Quasit(GlobalCreatureBaseClass):
    """
    Quasit creature
    Size: Tiny, Type: Fiend (Demon, Shapechanger), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 7,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "Fiend (Demon, Shapechanger), chaotic evil",
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
        self.abilities.extend(['shapechanger'])

    def shapechanger(self) -> str:
        """Shapechanger: The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly ..."""
        return "The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true "
    def shapechanger(self) -> str:
        """Shapechanger: The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly ..."""
        return "The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true "

