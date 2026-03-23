# bases1/young-red-shadow-dragon.py
"""
YoungRedShadowDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-red-shadow-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungRedShadowDragon(GlobalCreatureBaseClass):
    """
    YoungRedShadowDragon creature
    Size: Large, Type: dragon, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 178,
        "min_level": 14,
        "level": 14,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "dragon, chaotic evil",
        "hit_points_up": [17, 17, 17],
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
        self.abilities.extend(['living_shadow'])

    def living_shadow(self) -> str:
        """Living Shadow: While in dim light or darkness, the dragon has resistance to damage that isn't force, psychic, or ra..."""
        return "While in dim light or darkness, the dragon has resistance to damage that isn't force, psychic, or radiant.Shadow Stealth. While in dim light or darkness, the dragon can take the Hide action as a bonus"
    def living_shadow(self) -> str:
        """Living Shadow: While in dim light or darkness, the dragon has resistance to damage that isn't force, psychic, or ra..."""
        return "While in dim light or darkness, the dragon has resistance to damage that isn't force, psychic, or radiant.Shadow Stealth. While in dim light or darkness, the dragon can take the Hide action as a bonus"

