# bases1/violet-fungus.py
"""
VioletFungus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=violet-fungus
"""
from creature_base import GlobalCreatureBaseClass


class VioletFungus(GlobalCreatureBaseClass):
    """
    VioletFungus creature
    Size: Medium, Type: plant, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 18,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 5,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "plant, unaligned",
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus.ActionsM..."""
        return "While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus.ActionsMultiattack. The fungus makes 1d4 Rotting Touch attacks.Rotting Touch. Melee Weapon Attack: +2 to hit"
    def false_appearance(self) -> str:
        """False Appearance: While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus.ActionsM..."""
        return "While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus.ActionsMultiattack. The fungus makes 1d4 Rotting Touch attacks.Rotting Touch. Melee Weapon Attack: +2 to hit"

