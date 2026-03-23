# bases1/demogorgon.py
"""
Demogorgon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=demogorgon
"""
from creature_base import GlobalCreatureBaseClass


class Demogorgon(GlobalCreatureBaseClass):
    """
    Demogorgon creature
    Size: Huge, Type: Fiend (Demon), Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 464,
        "min_level": 27,
        "level": 27,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 22,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Fiend (Demon), Chaotic Evil",
        "hit_points_up": [46, 46, 46],
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
        """Legendary Resistance (3/Day): If Demogorgon fails a saving throw, he can choose to succeed instead.Magic Resistance. Demogorgon ha..."""
        return "If Demogorgon fails a saving throw, he can choose to succeed instead.Magic Resistance. Demogorgon has advantage on saving throws against spells and other magical effects.Two Heads. Demogorgon has adva"

