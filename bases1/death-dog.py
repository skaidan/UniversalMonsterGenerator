# bases1/death-dog.py
"""
DeathDog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-dog
"""
from creature_base import GlobalCreatureBaseClass


class DeathDog(GlobalCreatureBaseClass):
    """
    DeathDog creature
    Size: Medium, Type: monstrosity, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 39,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "monstrosity, neutral evil",
        "hit_points_up": [3, 3, 3],
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
        self.abilities.extend(['twoheaded'])

    def twoheaded(self) -> str:
        """Two-Headed: The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, char..."""
        return "The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious.ActionsMultiattack. The dog makes two bit"
    def twoheaded(self) -> str:
        """Two-Headed: The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, char..."""
        return "The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious.ActionsMultiattack. The dog makes two bit"

