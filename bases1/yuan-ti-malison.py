# bases1/yuan-ti-malison.py
"""
YuanTiMalison creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-malison
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiMalison(GlobalCreatureBaseClass):
    """
    YuanTiMalison creature
    Size: Medium, Type: snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 66,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.",
        "hit_points_up": [6, 6, 6],
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
        """Shapechanger: The yuan-ti can use its action to polymorph into a Medium snake, or back into its true form. Its sta..."""
        return "The yuan-ti can use its action to polymorph into a Medium snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doe"
    def shapechanger(self) -> str:
        """Shapechanger: The yuan-ti can use its action to polymorph into a Medium snake, or back into its true form. Its sta..."""
        return "The yuan-ti can use its action to polymorph into a Medium snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doe"

