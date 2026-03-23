# bases1/drake-companion.py
"""
DrakeCompanion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drake-companion
"""
from creature_base import GlobalCreatureBaseClass


class DrakeCompanion(GlobalCreatureBaseClass):
    """
    DrakeCompanion creature
    Size: Small, Type: dragon, -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 5,
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
        "size": "Small",
        "type": "dragon, -",
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
        self.abilities.extend(['draconic_essence'])

    def draconic_essence(self) -> str:
        """Draconic Essence: When you summon the drake, choose a damage type: acid, cold, fire, lightning, or poison. The chosen ..."""
        return "When you summon the drake, choose a damage type: acid, cold, fire, lightning, or poison. The chosen type determines the drake's damage immunity and the damage of its Infused Strikes trait.ActionsBite."

