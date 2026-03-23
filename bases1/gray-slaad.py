# bases1/gray-slaad.py
"""
GraySlaad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gray-slaad
"""
from creature_base import GlobalCreatureBaseClass


class GraySlaad(GlobalCreatureBaseClass):
    """
    GraySlaad creature
    Size: Small, Type: or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 127,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
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
        """Shapechanger: The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true for..."""
        return "The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or ca"
    def shapechanger(self) -> str:
        """Shapechanger: The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true for..."""
        return "The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or ca"

