# bases1/merregon.py
"""
Merregon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merregon
"""
from creature_base import GlobalCreatureBaseClass


class Merregon(GlobalCreatureBaseClass):
    """
    Merregon creature
    Size: Medium, Type: Fiend (Devil), typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 5,
        "level": 5,
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
        "type": "Fiend (Devil), typically Lawful Evil",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the merregon's darkvision.Magic Resistance. The merregon has advanta..."""
        return "Magical darkness doesn't impede the merregon's darkvision.Magic Resistance. The merregon has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The merregon makes "

