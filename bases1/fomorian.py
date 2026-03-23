# bases1/fomorian.py
"""
Fomorian creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fomorian
"""
from creature_base import GlobalCreatureBaseClass


class Fomorian(GlobalCreatureBaseClass):
    """
    Fomorian creature
    Size: Huge, Type: giant, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 149,
        "min_level": 9,
        "level": 9,
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
        "type": "giant, chaotic evil",
        "hit_points_up": [14, 14, 14],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The fomorian attacks twice with its greatclub or makes one greatclub attack and uses Evil Eye once.G..."""
        return "The fomorian attacks twice with its greatclub or makes one greatclub attack and uses Evil Eye once.Greatclub. Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 19 (3d8 + 6) bludgeoning da"
    def multiattack(self) -> str:
        """Multiattack: The fomorian attacks twice with its greatclub or makes one greatclub attack and uses Evil Eye once.G..."""
        return "The fomorian attacks twice with its greatclub or makes one greatclub attack and uses Evil Eye once.Greatclub. Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 19 (3d8 + 6) bludgeoning da"

