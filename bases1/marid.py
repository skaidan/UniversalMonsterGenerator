# bases1/marid.py
"""
Marid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=marid
"""
from creature_base import GlobalCreatureBaseClass


class Marid(GlobalCreatureBaseClass):
    """
    Marid creature
    Size: Huge, Type: or smaller, is pushed up to 20 feet away from the marid and knocked prone. On a success, a target takes half the bludgeoning damage, but is neither pushed nor knocked prone.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 229,
        "min_level": 12,
        "level": 12,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "or smaller, is pushed up to 20 feet away from the marid and knocked prone. On a success, a target takes half the bludgeoning damage, but is neither pushed nor knocked prone.",
        "hit_points_up": [22, 22, 22],
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
        """Amphibious: The marid can breathe air and water.Elemental Demise. If the marid dies, its body disintegrates into..."""
        return "The marid can breathe air and water.Elemental Demise. If the marid dies, its body disintegrates into a burst of water and foam, leaving behind only equipment the marid was wearing or carrying.Innate S"
    def amphibious(self) -> str:
        """Amphibious: The marid can breathe air and water.Elemental Demise. If the marid dies, its body disintegrates into..."""
        return "The marid can breathe air and water.Elemental Demise. If the marid dies, its body disintegrates into a burst of water and foam, leaving behind only equipment the marid was wearing or carrying.Innate S"

