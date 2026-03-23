# bases1/zariel.py
"""
Zariel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zariel
"""
from creature_base import GlobalCreatureBaseClass


class Zariel(GlobalCreatureBaseClass):
    """
    Zariel creature
    Size: Medium, Type: when changing her appearance),
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 420,
        "min_level": 27,
        "level": 27,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 21,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "when changing her appearance),",
        "hit_points_up": [42, 42, 42],
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
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede Zariel's darkvision.Legendary Resistance (3/Day). If Zariel fails a ..."""
        return "Magical darkness doesn't impede Zariel's darkvision.Legendary Resistance (3/Day). If Zariel fails a saving throw, she can choose to succeed instead.Magic Resistance. Zariel has advantage on saving thr"

