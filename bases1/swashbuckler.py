# bases1/swashbuckler.py
"""
Swashbuckler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swashbuckler
"""
from creature_base import GlobalCreatureBaseClass


class Swashbuckler(GlobalCreatureBaseClass):
    """
    Swashbuckler creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 66,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
        "hit_points_up": [6, 6, 6],
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
        self.abilities.extend(['suave_defense'])

    def suave_defense(self) -> str:
        """Suave Defense: While the swashbuckler is wearing light or no armor and wielding no shield, its AC includes its Char..."""
        return "While the swashbuckler is wearing light or no armor and wielding no shield, its AC includes its Charisma modifier.ActionsMultiattack. The swashbuckler makes one Dagger attack and two Rapier attacks.Da"

