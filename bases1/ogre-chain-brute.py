# bases1/ogre-chain-brute.py
"""
OgreChainBrute creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ogre-chain-brute
"""
from creature_base import GlobalCreatureBaseClass


class OgreChainBrute(GlobalCreatureBaseClass):
    """
    OgreChainBrute creature
    Size: Large, Type: Giant, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 59,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Giant, typically Chaotic Evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['fist'])

    def fist(self) -> str:
        """Fist: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.Chain S..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.Chain Smash (Recharge 6). Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) bludg"

