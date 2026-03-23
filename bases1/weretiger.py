# bases1/weretiger.py
"""
Weretiger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=weretiger
"""
from creature_base import GlobalCreatureBaseClass


class Weretiger(GlobalCreatureBaseClass):
    """
    Weretiger creature
    Size: Medium, Type: humanoid (Human, Shapechanger), neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 120,
        "min_level": 5,
        "level": 5,
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
        "type": "humanoid (Human, Shapechanger), neutral",
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
        """Shapechanger: The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back ..."""
        return "The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for"
    def shapechanger(self) -> str:
        """Shapechanger: The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back ..."""
        return "The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for"

