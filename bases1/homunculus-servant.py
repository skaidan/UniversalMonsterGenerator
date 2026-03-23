# bases1/homunculus-servant.py
"""
HomunculusServant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=homunculus-servant
"""
from creature_base import GlobalCreatureBaseClass


class HomunculusServant(GlobalCreatureBaseClass):
    """
    HomunculusServant creature
    Size: Tiny, Type: construct, -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 1,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "construct, -",
        "hit_points_up": [1, 1, 1],
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
        """Evasion: If the homunculus is subjected to an effect that allows it to make a Dexterity saving throw to take ..."""
        return "If the homunculus is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damag"

