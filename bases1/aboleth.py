# bases1/aboleth.py
"""
Aboleth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=aboleth
"""
from creature_base import GlobalCreatureBaseClass


class Aboleth(GlobalCreatureBaseClass):
    """
    Aboleth creature
    Size: Large, Type: aberration, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 135,
        "min_level": 11,
        "level": 11,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "aberration, lawful evil",
        "hit_points_up": [13, 13, 13],
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
        """Amphibious: The aboleth can breathe air and water.Mucous Cloud. While underwater, the aboleth is surrounded by t..."""
        return "The aboleth can breathe air and water.Mucous Cloud. While underwater, the aboleth is surrounded by transformative mucus. A creature that touches the aboleth or that hits it with a melee attack while w"
    def amphibious(self) -> str:
        """Amphibious: The aboleth can breathe air and water.Mucous Cloud. While underwater, the aboleth is surrounded by t..."""
        return "The aboleth can breathe air and water.Mucous Cloud. While underwater, the aboleth is surrounded by transformative mucus. A creature that touches the aboleth or that hits it with a melee attack while w"

