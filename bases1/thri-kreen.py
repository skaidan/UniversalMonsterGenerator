# bases1/thri-kreen.py
"""
ThriKreen creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=thri-kreen
"""
from creature_base import GlobalCreatureBaseClass


class ThriKreen(GlobalCreatureBaseClass):
    """
    ThriKreen creature
    Size: Medium, Type: humanoid (Thri-kreen), chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
        "min_level": 2,
        "level": 2,
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
        "type": "humanoid (Thri-kreen), chaotic neutral",
        "hit_points_up": [3, 3, 3],
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
        self.abilities.extend(['chameleon_carapace'])

    def chameleon_carapace(self) -> str:
        """Chameleon Carapace: The thri-kreen can change the color of its carapace to match the color and texture of its surroundin..."""
        return "The thri-kreen can change the color of its carapace to match the color and texture of its surroundings. As a result, it has advantage on Dexterity (Stealth) checks made to hide.Standing Leap. The thri"
    def chameleon_carapace(self) -> str:
        """Chameleon Carapace: The thri-kreen can change the color of its carapace to match the color and texture of its surroundin..."""
        return "The thri-kreen can change the color of its carapace to match the color and texture of its surroundings. As a result, it has advantage on Dexterity (Stealth) checks made to hide.Standing Leap. The thri"

