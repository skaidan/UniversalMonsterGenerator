# bases1/red-slaad.py
"""
RedSlaad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=red-slaad
"""
from creature_base import GlobalCreatureBaseClass


class RedSlaad(GlobalCreatureBaseClass):
    """
    RedSlaad creature
    Size: Large, Type: aberration, chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 93,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "aberration, chaotic neutral",
        "hit_points_up": [9, 9, 9],
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The ..."""
        return "The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The slaad regains 10 hit points at the start of its turn if it has at least 1 hit point.ActionsMultiatta"
    def magic_resistance(self) -> str:
        """Magic Resistance: The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The ..."""
        return "The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The slaad regains 10 hit points at the start of its turn if it has at least 1 hit point.ActionsMultiatta"

