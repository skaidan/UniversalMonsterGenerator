# bases1/adult-gold-dragon.py
"""
AdultGoldDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-gold-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultGoldDragon(GlobalCreatureBaseClass):
    """
    AdultGoldDragon creature
    Size: Huge, Type: dragon (Metallic), lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 256,
        "min_level": 18,
        "level": 18,
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
        "type": "dragon (Metallic), lawful good",
        "hit_points_up": [25, 25, 25],
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

