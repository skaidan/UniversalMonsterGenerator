# bases1/mud-mephit.py
"""
MudMephit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mud-mephit
"""
from creature_base import GlobalCreatureBaseClass


class MudMephit(GlobalCreatureBaseClass):
    """
    MudMephit creature
    Size: Medium, Type: or smaller, it must succeed on a DC 11 Dexterity saving throw or be restrained for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 27,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, it must succeed on a DC 11 Dexterity saving throw or be restrained for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['death_burst'])

    def death_burst(self) -> str:
        """Death Burst: When the mephit dies, it explodes in a burst of sticky mud. Each Medium or smaller creature within 5..."""
        return "When the mephit dies, it explodes in a burst of sticky mud. Each Medium or smaller creature within 5 feet of it must succeed on a DC 11 Dexterity saving throw or be restrained until the end of the cre"
    def death_burst(self) -> str:
        """Death Burst: When the mephit dies, it explodes in a burst of sticky mud. Each Medium or smaller creature within 5..."""
        return "When the mephit dies, it explodes in a burst of sticky mud. Each Medium or smaller creature within 5 feet of it must succeed on a DC 11 Dexterity saving throw or be restrained until the end of the cre"

