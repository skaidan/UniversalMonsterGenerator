# bases1/boneclaw.py
"""
Boneclaw creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=boneclaw
"""
from creature_base import GlobalCreatureBaseClass


class Boneclaw(GlobalCreatureBaseClass):
    """
    Boneclaw creature
    Size: Large, Type: Undead, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 150,
        "min_level": 13,
        "level": 13,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Undead, typically Chaotic Evil",
        "hit_points_up": [15, 15, 15],
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
        self.abilities.extend(['rejuvenation'])

    def rejuvenation(self) -> str:
        """Rejuvenation: While its master lives, a destroyed boneclaw gains a new body in 1d10 hours, with all its hit points..."""
        return "While its master lives, a destroyed boneclaw gains a new body in 1d10 hours, with all its hit points. The new body appears within 1 mile of the boneclaw's master.Unusual Nature. The boneclaw doesn't r"

