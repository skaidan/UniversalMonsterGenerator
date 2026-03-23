# bases1/xvart.py
"""
Xvart creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=xvart
"""
from creature_base import GlobalCreatureBaseClass


class Xvart(GlobalCreatureBaseClass):
    """
    Xvart creature
    Size: Medium, Type: or smaller creature.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 7,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature.",
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
        # Add creature-specific abilities
        self.abilities.extend(['raxivorts_tongue'])

    def raxivorts_tongue(self) -> str:
        """Raxivort's Tongue: The xvart can communicate with ordinary bats and rats, as well as giant bats and giant rats.ActionsS..."""
        return "The xvart can communicate with ordinary bats and rats, as well as giant bats and giant rats.ActionsShortsword. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage"

