# bases1/displacer-beast.py
"""
DisplacerBeast creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=displacer-beast
"""
from creature_base import GlobalCreatureBaseClass


class DisplacerBeast(GlobalCreatureBaseClass):
    """
    DisplacerBeast creature
    Size: Large, Type: monstrosity, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 85,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, lawful evil",
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
        """Avoidance: If the displacer beast is subjected to an effect that allows it to make a saving throw to take only ..."""
        return "If the displacer beast is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if "
    def avoidance(self) -> str:
        """Avoidance: If the displacer beast is subjected to an effect that allows it to make a saving throw to take only ..."""
        return "If the displacer beast is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if "

