# bases1/treant.py
"""
Treant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=treant
"""
from creature_base import GlobalCreatureBaseClass


class Treant(GlobalCreatureBaseClass):
    """
    Treant creature
    Size: Huge, Type: plant, chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 138,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "plant, chaotic good",
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the treant remains motionless, it is indistinguishable from a normal tree.Siege Monster. The t..."""
        return "While the treant remains motionless, it is indistinguishable from a normal tree.Siege Monster. The treant deals double damage to objects and structures.ActionsMultiattack. The treant makes two slam at"
    def false_appearance(self) -> str:
        """False Appearance: While the treant remains motionless, it is indistinguishable from a normal tree.Siege Monster. The t..."""
        return "While the treant remains motionless, it is indistinguishable from a normal tree.Siege Monster. The treant deals double damage to objects and structures.ActionsMultiattack. The treant makes two slam at"

