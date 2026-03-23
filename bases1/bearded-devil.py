# bases1/bearded-devil.py
"""
BeardedDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bearded-devil
"""
from creature_base import GlobalCreatureBaseClass


class BeardedDevil(GlobalCreatureBaseClass):
    """
    BeardedDevil creature
    Size: Medium, Type: fiend (Devil), lawful evil
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
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fiend (Devil), lawful evil",
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
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on ..."""
        return "Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects.Steadfast. The devil can't be frightened whil"
    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on ..."""
        return "Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects.Steadfast. The devil can't be frightened whil"

