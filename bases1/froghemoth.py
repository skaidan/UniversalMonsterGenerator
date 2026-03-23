# bases1/froghemoth.py
"""
Froghemoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=froghemoth
"""
from creature_base import GlobalCreatureBaseClass


class Froghemoth(GlobalCreatureBaseClass):
    """
    Froghemoth creature
    Size: Medium, Type: or smaller creature that it can see within 20 feet of it. The target must make a DC 18 Strength saving throw. On a failed save, the target is pulled into an unoccupied space within 5 feet of the froghemoth.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 161,
        "min_level": 11,
        "level": 11,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature that it can see within 20 feet of it. The target must make a DC 18 Strength saving throw. On a failed save, the target is pulled into an unoccupied space within 5 feet of the froghemoth.",
        "hit_points_up": [16, 16, 16],
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The froghemoth can breathe air and water.Shock Susceptibility. If the froghemoth takes lightning dam..."""
        return "The froghemoth can breathe air and water.Shock Susceptibility. If the froghemoth takes lightning damage, it suffers two effects until the end of its next turn: its speed is halved, and it has disadvan"

