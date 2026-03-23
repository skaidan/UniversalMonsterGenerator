# bases1/redcap.py
"""
Redcap creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=redcap
"""
from creature_base import GlobalCreatureBaseClass


class Redcap(GlobalCreatureBaseClass):
    """
    Redcap creature
    Size: Small, Type: Fey, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "Fey, typically Chaotic Evil",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['iron_boots'])

    def iron_boots(self) -> str:
        """Iron Boots: The redcap has disadvantage on Dexterity (Stealth) checks.Outsize Strength. While grappling, the red..."""
        return "The redcap has disadvantage on Dexterity (Stealth) checks.Outsize Strength. While grappling, the redcap is considered to be Medium. Also, wielding a heavy weapon doesn't impose disadvantage on its att"

