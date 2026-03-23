# bases1/winter-eladrin.py
"""
WinterEladrin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=winter-eladrin
"""
from creature_base import GlobalCreatureBaseClass


class WinterEladrin(GlobalCreatureBaseClass):
    """
    WinterEladrin creature
    Size: Medium, Type: Fey (Elf), typically Chaotic Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 165,
        "min_level": 11,
        "level": 11,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fey (Elf), typically Chaotic Neutral",
        "hit_points_up": [16, 16, 16],
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The eladrin has advantage on saving throws against spells and other magical effects.Sorrowful Presen..."""
        return "The eladrin has advantage on saving throws against spells and other magical effects.Sorrowful Presence. Any non-eladrin creature that starts its turn within 60 feet of the eladrin must make a DC 13 Wi"

