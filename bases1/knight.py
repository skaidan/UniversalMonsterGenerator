# bases1/knight.py
"""
Knight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=knight
"""
from creature_base import GlobalCreatureBaseClass


class Knight(GlobalCreatureBaseClass):
    """
    Knight creature
    Size: Medium, Type: humanoid (any race), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
        "min_level": 4,
        "level": 4,
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
        "type": "humanoid (any race), any alignment",
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
        self.abilities.extend(['brave'])

    def brave(self) -> str:
        """Brave: The knight has advantage on saving throws against being frightened.ActionsMultiattack. The knight ma..."""
        return "The knight has advantage on saving throws against being frightened.ActionsMultiattack. The knight makes two melee attacks.Greatsword. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 ("
    def brave(self) -> str:
        """Brave: The knight has advantage on saving throws against being frightened.ActionsMultiattack. The knight ma..."""
        return "The knight has advantage on saving throws against being frightened.ActionsMultiattack. The knight makes two melee attacks.Greatsword. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 ("

