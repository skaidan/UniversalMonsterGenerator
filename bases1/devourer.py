# bases1/devourer.py
"""
Devourer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=devourer
"""
from creature_base import GlobalCreatureBaseClass


class Devourer(GlobalCreatureBaseClass):
    """
    Devourer creature
    Size: Large, Type: Undead, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 189,
        "min_level": 14,
        "level": 14,
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
        "hit_points_up": [18, 18, 18],
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
        self.abilities.extend(['unusual_nature'])

    def unusual_nature(self) -> str:
        """Unusual Nature: A devourer doesn't require air, drink, or sleep.ActionsMultiattack. The devourer makes two Claw atta..."""
        return "A devourer doesn't require air, drink, or sleep.ActionsMultiattack. The devourer makes two Claw attacks and can use either Imprison Soul or Soul Rend, if available.Claw. Melee Weapon Attack: +10 to hi"

