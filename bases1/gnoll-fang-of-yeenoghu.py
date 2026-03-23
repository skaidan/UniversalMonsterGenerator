# bases1/gnoll-fang-of-yeenoghu.py
"""
GnollFangOfYeenoghu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll-fang-of-yeenoghu
"""
from creature_base import GlobalCreatureBaseClass


class GnollFangOfYeenoghu(GlobalCreatureBaseClass):
    """
    GnollFangOfYeenoghu creature
    Size: Medium, Type: fiend (Gnoll), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 65,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fiend (Gnoll), chaotic evil",
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
        self.abilities.extend(['rampage'])

    def rampage(self) -> str:
        """Rampage: When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can tak..."""
        return "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack.ActionsMultiattack. The gnoll m"
    def rampage(self) -> str:
        """Rampage: When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can tak..."""
        return "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack.ActionsMultiattack. The gnoll m"

