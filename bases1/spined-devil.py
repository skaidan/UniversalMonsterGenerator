# bases1/spined-devil.py
"""
SpinedDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spined-devil
"""
from creature_base import GlobalCreatureBaseClass


class SpinedDevil(GlobalCreatureBaseClass):
    """
    SpinedDevil creature
    Size: Small, Type: fiend (Devil), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "fiend (Devil), lawful evil",
        "hit_points_up": [2, 2, 2],
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
        """Devil's Sight: Magical darkness doesn't impede the devil's darkvision.Flyby. The devil doesn't provoke an opportuni..."""
        return "Magical darkness doesn't impede the devil's darkvision.Flyby. The devil doesn't provoke an opportunity attack when it flies out of an enemy's reach.Limited Spines. The devil has twelve tail spines. Us"
    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the devil's darkvision.Flyby. The devil doesn't provoke an opportuni..."""
        return "Magical darkness doesn't impede the devil's darkvision.Flyby. The devil doesn't provoke an opportunity attack when it flies out of an enemy's reach.Limited Spines. The devil has twelve tail spines. Us"

