# bases1/adult-white-dragon.py
"""
AdultWhiteDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-white-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultWhiteDragon(GlobalCreatureBaseClass):
    """
    AdultWhiteDragon creature
    Size: Huge, Type: dragon (Chromatic), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 200,
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
        "size": "Huge",
        "type": "dragon (Chromatic), chaotic evil",
        "hit_points_up": [20, 20, 20],
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
        self.abilities.extend(['ice_walk'])

    def ice_walk(self) -> str:
        """Ice Walk: The dragon can move across and climb icy surfaces without needing to make an ability check. Addition..."""
        return "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra moment.Legendary Resistance (3"
    def ice_walk(self) -> str:
        """Ice Walk: The dragon can move across and climb icy surfaces without needing to make an ability check. Addition..."""
        return "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra moment.Legendary Resistance (3"

