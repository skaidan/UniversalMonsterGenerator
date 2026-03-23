# bases1/merrow.py
"""
Merrow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merrow
"""
from creature_base import GlobalCreatureBaseClass


class Merrow(GlobalCreatureBaseClass):
    """
    Merrow creature
    Size: Huge, Type: or smaller creature, it must succeed on a Strength contest against the merrow or be pulled up to 20 feet toward the merrow.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "or smaller creature, it must succeed on a Strength contest against the merrow or be pulled up to 20 feet toward the merrow.",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The merrow can breathe air and water.ActionsMultiattack. The merrow makes two attacks: one with its ..."""
        return "The merrow can breathe air and water.ActionsMultiattack. The merrow makes two attacks: one with its bite and one with its claws or harpoon.Bite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target"
    def amphibious(self) -> str:
        """Amphibious: The merrow can breathe air and water.ActionsMultiattack. The merrow makes two attacks: one with its ..."""
        return "The merrow can breathe air and water.ActionsMultiattack. The merrow makes two attacks: one with its bite and one with its claws or harpoon.Bite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target"

