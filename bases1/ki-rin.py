# bases1/ki-rin.py
"""
KiRin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ki-rin
"""
from creature_base import GlobalCreatureBaseClass


class KiRin(GlobalCreatureBaseClass):
    """
    KiRin creature
    Size: Large, Type: Celestial, typically Lawful Good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 153,
        "min_level": 13,
        "level": 13,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Celestial, typically Lawful Good",
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
        self.abilities.extend(['legendary_resistance_day'])

    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (3/Day): If the ki-rin fails a saving throw, it can choose to succeed instead.Magic Resistance. The ki-rin ha..."""
        return "If the ki-rin fails a saving throw, it can choose to succeed instead.Magic Resistance. The ki-rin has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The ki-rin"

