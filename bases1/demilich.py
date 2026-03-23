# bases1/demilich.py
"""
Demilich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=demilich
"""
from creature_base import GlobalCreatureBaseClass


class Demilich(GlobalCreatureBaseClass):
    """
    Demilich creature
    Size: Tiny, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 80,
        "min_level": 19,
        "level": 19,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "undead, neutral evil",
        "hit_points_up": [8, 8, 8],
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
        self.abilities.extend(['avoidance'])

    def avoidance(self) -> str:
        """Avoidance: If the demilich is subjected to an effect that allows it to make a saving throw to take only half da..."""
        return "If the demilich is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fail"
    def avoidance(self) -> str:
        """Avoidance: If the demilich is subjected to an effect that allows it to make a saving throw to take only half da..."""
        return "If the demilich is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fail"

