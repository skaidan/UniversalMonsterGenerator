# bases1/red-abishai.py
"""
RedAbishai creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=red-abishai
"""
from creature_base import GlobalCreatureBaseClass


class RedAbishai(GlobalCreatureBaseClass):
    """
    RedAbishai creature
    Size: Medium, Type: Fiend (Devil), typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 289,
        "min_level": 20,
        "level": 20,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 22,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fiend (Devil), typically Lawful Evil",
        "hit_points_up": [28, 28, 28],
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
        """Devil's Sight: Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage..."""
        return "Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The abishai makes one"

