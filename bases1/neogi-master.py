# bases1/neogi-master.py
"""
NeogiMaster creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=neogi-master
"""
from creature_base import GlobalCreatureBaseClass


class NeogiMaster(GlobalCreatureBaseClass):
    """
    NeogiMaster creature
    Size: Medium, Type: Aberration (Warlock), typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 71,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Aberration (Warlock), typically Lawful Evil",
        "hit_points_up": [7, 7, 7],
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
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the neogi's darkvision.Mental Fortitude. The neogi has advantage on ..."""
        return "Magical darkness doesn't impede the neogi's darkvision.Mental Fortitude. The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Cli"

