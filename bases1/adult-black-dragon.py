# bases1/adult-black-dragon.py
"""
AdultBlackDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-black-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultBlackDragon(GlobalCreatureBaseClass):
    """
    AdultBlackDragon creature
    Size: Huge, Type: dragon (Chromatic), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 195,
        "min_level": 15,
        "level": 15,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "dragon (Chromatic), chaotic evil",
        "hit_points_up": [19, 19, 19],
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
        """Amphibious: The dragon can breathe air and water.Legendary Resistance (3/Day). If the dragon fails a saving thro..."""
        return "The dragon can breathe air and water.Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon can use its Frightful Presence. I"
    def amphibious(self) -> str:
        """Amphibious: The dragon can breathe air and water.Legendary Resistance (3/Day). If the dragon fails a saving thro..."""
        return "The dragon can breathe air and water.Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead.ActionsMultiattack. The dragon can use its Frightful Presence. I"

