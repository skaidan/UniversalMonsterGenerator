# bases1/gargoyle.py
"""
Gargoyle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gargoyle
"""
from creature_base import GlobalCreatureBaseClass


class Gargoyle(GlobalCreatureBaseClass):
    """
    Gargoyle creature
    Size: Medium, Type: elemental, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
        "min_level": 3,
        "level": 3,
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
        "type": "elemental, chaotic evil",
        "hit_points_up": [5, 5, 5],
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
        """False Appearance: While the gargoyle remains motionless, it is indistinguishable from an inanimate statue.ActionsMulti..."""
        return "While the gargoyle remains motionless, it is indistinguishable from an inanimate statue.ActionsMultiattack. The gargoyle makes two attacks: one with its bite and one with its claws.Bite. Melee Weapon "
    def false_appearance(self) -> str:
        """False Appearance: While the gargoyle remains motionless, it is indistinguishable from an inanimate statue.ActionsMulti..."""
        return "While the gargoyle remains motionless, it is indistinguishable from an inanimate statue.ActionsMultiattack. The gargoyle makes two attacks: one with its bite and one with its claws.Bite. Melee Weapon "

