# bases1/grimlock.py
"""
Grimlock creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grimlock
"""
from creature_base import GlobalCreatureBaseClass


class Grimlock(GlobalCreatureBaseClass):
    """
    Grimlock creature
    Size: Medium, Type: humanoid (Grimlock), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Grimlock), neutral evil",
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
        self.abilities.extend(['blind_senses'])

    def blind_senses(self) -> str:
        """Blind Senses: The grimlock can't use its blindsight while deafened and unable to smell.Keen Hearing and Smell. The..."""
        return "The grimlock can't use its blindsight while deafened and unable to smell.Keen Hearing and Smell. The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell.Stone Camouflage"
    def blind_senses(self) -> str:
        """Blind Senses: The grimlock can't use its blindsight while deafened and unable to smell.Keen Hearing and Smell. The..."""
        return "The grimlock can't use its blindsight while deafened and unable to smell.Keen Hearing and Smell. The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell.Stone Camouflage"

