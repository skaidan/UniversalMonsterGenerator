# bases1/archer.py
"""
Archer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=archer
"""
from creature_base import GlobalCreatureBaseClass


class Archer(GlobalCreatureBaseClass):
    """
    Archer creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 75,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
        "hit_points_up": [7, 7, 7],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The archer makes two Shortsword or Longbow attacks.Shortsword. Melee Weapon Attack: +6 to hit, reach..."""
        return "The archer makes two Shortsword or Longbow attacks.Shortsword. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage.Longbow. Ranged Weapon Attack: +6 to hit, range"

