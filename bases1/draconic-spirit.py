# bases1/draconic-spirit.py
"""
DraconicSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconic-spirit
"""
from creature_base import GlobalCreatureBaseClass


class DraconicSpirit(GlobalCreatureBaseClass):
    """
    DraconicSpirit creature
    Size: Large, Type: dragon, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 50,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "dragon, neutral",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['shared_resistances'])

    def shared_resistances(self) -> str:
        """Shared Resistances: When you summon the dragon, choose one of its damage resistances. You have resistance to the chosen ..."""
        return "When you summon the dragon, choose one of its damage resistances. You have resistance to the chosen damage type until the spell ends.ActionsMultiattack. The dragon makes a number of Rend attacks equal"

