# bases1/bone-devil.py
"""
BoneDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bone-devil
"""
from creature_base import GlobalCreatureBaseClass


class BoneDevil(GlobalCreatureBaseClass):
    """
    BoneDevil creature
    Size: Large, Type: fiend (Devil), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 142,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend (Devil), lawful evil",
        "hit_points_up": [14, 14, 14],
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
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on ..."""
        return "Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The devil makes three att"
    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on ..."""
        return "Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The devil makes three att"

