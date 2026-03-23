# bases1/meenlock.py
"""
Meenlock creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=meenlock
"""
from creature_base import GlobalCreatureBaseClass


class Meenlock(GlobalCreatureBaseClass):
    """
    Meenlock creature
    Size: Small, Type: Fey, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 31,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "Fey, typically Neutral Evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['fear_aura'])

    def fear_aura(self) -> str:
        """Fear Aura: Any Beast or Humanoid that starts its turn within 10 feet of the meenlock must succeed on a DC 11 Wi..."""
        return "Any Beast or Humanoid that starts its turn within 10 feet of the meenlock must succeed on a DC 11 Wisdom saving throw or be frightened until the start of the creature's next turn.Light Sensitivity. Wh"

