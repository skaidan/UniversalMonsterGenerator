# bases1/yuan-ti-abomination.py
"""
YuanTiAbomination creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-abomination
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiAbomination(GlobalCreatureBaseClass):
    """
    YuanTiAbomination creature
    Size: Large, Type: snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 127,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.",
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
        self.abilities.extend(['shapechanger'])

    def shapechanger(self) -> str:
        """Shapechanger: The yuan-ti can use its action to polymorph into a Large snake, or back into its true form. Its stat..."""
        return "The yuan-ti can use its action to polymorph into a Large snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It does"
    def shapechanger(self) -> str:
        """Shapechanger: The yuan-ti can use its action to polymorph into a Large snake, or back into its true form. Its stat..."""
        return "The yuan-ti can use its action to polymorph into a Large snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It does"

