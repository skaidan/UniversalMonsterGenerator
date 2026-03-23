# bases1/martial-arts-adept.py
"""
MartialArtsAdept creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=martial-arts-adept
"""
from creature_base import GlobalCreatureBaseClass


class MartialArtsAdept(GlobalCreatureBaseClass):
    """
    MartialArtsAdept creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 60,
        "min_level": 4,
        "level": 4,
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
        self.abilities.extend(['unarmored_defense'])

    def unarmored_defense(self) -> str:
        """Unarmored Defense: While the adept is wearing no armor and wielding no shield, its AC includes its Wisdom modifier.Acti..."""
        return "While the adept is wearing no armor and wielding no shield, its AC includes its Wisdom modifier.ActionsMultiattack. The adept makes three Unarmed Strike attacks or five Dart attacks.Unarmed Strike. Me"

