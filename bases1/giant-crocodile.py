# bases1/giant-crocodile.py
"""
GiantCrocodile creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-crocodile
"""
from creature_base import GlobalCreatureBaseClass


class GiantCrocodile(GlobalCreatureBaseClass):
    """
    GiantCrocodile creature
    Size: Huge, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 85,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast, unaligned",
        "hit_points_up": [8, 8, 8],
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The crocodile can hold its breath for 30 minutes.ActionsMultiattack. The crocodile makes two attacks..."""
        return "The crocodile can hold its breath for 30 minutes.ActionsMultiattack. The crocodile makes two attacks: one with its bite and one with its tail.Bite. Melee Weapon Attack: +8 to hit, reach 5 ft., one tar"
    def hold_breath(self) -> str:
        """Hold Breath: The crocodile can hold its breath for 30 minutes.ActionsMultiattack. The crocodile makes two attacks..."""
        return "The crocodile can hold its breath for 30 minutes.ActionsMultiattack. The crocodile makes two attacks: one with its bite and one with its tail.Bite. Melee Weapon Attack: +8 to hit, reach 5 ft., one tar"

