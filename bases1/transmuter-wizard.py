# bases1/transmuter-wizard.py
"""
TransmuterWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=transmuter-wizard
"""
from creature_base import GlobalCreatureBaseClass


class TransmuterWizard(GlobalCreatureBaseClass):
    """
    TransmuterWizard creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 49,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
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
        self.abilities.extend(['transmuters_stone'])

    def transmuters_stone(self) -> str:
        """Transmuter's Stone: The transmuter carries a magic stone it crafted. The stone grants it one of the following benefits w..."""
        return "The transmuter carries a magic stone it crafted. The stone grants it one of the following benefits while bearing the stone; the transmuter chooses the benefit at the end of each long rest:&nbsp; Darkv"

