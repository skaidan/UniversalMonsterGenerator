# bases1/master-thief.py
"""
MasterThief creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=master-thief
"""
from creature_base import GlobalCreatureBaseClass


class MasterThief(GlobalCreatureBaseClass):
    """
    MasterThief creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 84,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
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
        # Add creature-specific abilities
        self.abilities.extend(['evasion'])

    def evasion(self) -> str:
        """Evasion: If the thief is subjected to an effect that allows it to make a Dexterity saving throw to take only ..."""
        return "If the thief is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the thief instead takes no damage if it succeeds on the saving throw and only half dama"

