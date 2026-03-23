# bases1/champion.py
"""
Champion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=champion
"""
from creature_base import GlobalCreatureBaseClass


class Champion(GlobalCreatureBaseClass):
    """
    Champion creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 143,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
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
        # Add creature-specific abilities
        self.abilities.extend(['indomitable_day'])

    def indomitable_day(self) -> str:
        """Indomitable (2/Day): The champion rerolls a failed saving throw.ActionsMultiattack. The champion makes three Greatsword o..."""
        return "The champion rerolls a failed saving throw.ActionsMultiattack. The champion makes three Greatsword or Shortbow attacks.Greatsword. Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6"

