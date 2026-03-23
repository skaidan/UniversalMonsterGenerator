# bases1/shadow.py
"""
Shadow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadow
"""
from creature_base import GlobalCreatureBaseClass


class Shadow(GlobalCreatureBaseClass):
    """
    Shadow creature
    Size: Medium, Type: undead, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 16,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, chaotic evil",
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
        self.abilities.extend(['amorphous'])

    def amorphous(self) -> str:
        """Amorphous: The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While..."""
        return "The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While in dim light or darkness, the shadow can take the Hide action as a bonus action.Sunlight Weakness. "
    def amorphous(self) -> str:
        """Amorphous: The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While..."""
        return "The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While in dim light or darkness, the shadow can take the Hide action as a bonus action.Sunlight Weakness. "

