# bases1/avatar-of-death.py
"""
AvatarOfDeath creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=avatar-of-death
"""
from creature_base import GlobalCreatureBaseClass


class AvatarOfDeath(GlobalCreatureBaseClass):
    """
    AvatarOfDeath creature
    Size: Medium, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 10,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, neutral evil",
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
        self.abilities.extend(['incorporeal_movement'])

    def incorporeal_movement(self) -> str:
        """Incorporeal Movement: The avatar can move through other creatures and objects as if they were difficult terrain. It takes ..."""
        return "The avatar can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Turning Immunity. The avatar is immune to"

