# bases1/giant-octopus.py
"""
GiantOctopus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-octopus
"""
from creature_base import GlobalCreatureBaseClass


class GiantOctopus(GlobalCreatureBaseClass):
    """
    GiantOctopus creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
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
        "size": "Large",
        "type": "beast, unaligned",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: While out of water, the octopus can hold its breath for 1 hour.Underwater Camouflage. The octopus ha..."""
        return "While out of water, the octopus can hold its breath for 1 hour.Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.Water Breathing. The octopus can bre"
    def hold_breath(self) -> str:
        """Hold Breath: While out of water, the octopus can hold its breath for 1 hour.Underwater Camouflage. The octopus ha..."""
        return "While out of water, the octopus can hold its breath for 1 hour.Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.Water Breathing. The octopus can bre"

