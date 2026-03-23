# bases1/orc-red-fang-of-shargaas.py
"""
OrcRedFangOfShargaas creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-red-fang-of-shargaas
"""
from creature_base import GlobalCreatureBaseClass


class OrcRedFangOfShargaas(GlobalCreatureBaseClass):
    """
    OrcRedFangOfShargaas creature
    Size: Medium, Type: humanoid (Orc), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Orc), chaotic evil",
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
        self.abilities.extend(['cunning_action'])

    def cunning_action(self) -> str:
        """Cunning Action: On each of its turns, the orc can use a bonus action to take the Dash, Disengage, or Hide action.Han..."""
        return "On each of its turns, the orc can use a bonus action to take the Dash, Disengage, or Hide action.Hand of Shargaas. The orc deals 2 extra dice of damage when it hits a target with a weapon attack (incl"

