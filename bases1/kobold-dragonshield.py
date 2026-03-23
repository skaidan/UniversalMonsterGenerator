# bases1/kobold-dragonshield.py
"""
KoboldDragonshield creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kobold-dragonshield
"""
from creature_base import GlobalCreatureBaseClass


class KoboldDragonshield(GlobalCreatureBaseClass):
    """
    KoboldDragonshield creature
    Size: Small, Type: Dragon, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 44,
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
        "size": "Small",
        "type": "Dragon, any alignment",
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
        self.abilities.extend(['dragons_resistance'])

    def dragons_resistance(self) -> str:
        """Dragon's Resistance: The kobold has resistance to a type of damage based on the color of dragon that invested it with pow..."""
        return "The kobold has resistance to a type of damage based on the color of dragon that invested it with power (choose or roll a d10): 1–2, acid (black or copper); 3–4, cold (silver or white); 5–6, fire (bras"

