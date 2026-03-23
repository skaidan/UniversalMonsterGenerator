# bases1/nupperibo.py
"""
Nupperibo creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nupperibo
"""
from creature_base import GlobalCreatureBaseClass


class Nupperibo(GlobalCreatureBaseClass):
    """
    Nupperibo creature
    Size: Medium, Type: Fiend (Devil), typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fiend (Devil), typically Lawful Evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['cloud_of_vermin'])

    def cloud_of_vermin(self) -> str:
        """Cloud of Vermin: Any creature, other than a devil, that starts its turn within 20 feet of one or more nupperibos must..."""
        return "Any creature, other than a devil, that starts its turn within 20 feet of one or more nupperibos must succeed on a DC 11 Constitution saving throw or take 5 (2d4) acid damage. A creature within the are"

