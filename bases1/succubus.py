# bases1/succubus.py
"""
Succubus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=succubus
"""
from creature_base import GlobalCreatureBaseClass


class Succubus(GlobalCreatureBaseClass):
    """
    Succubus creature
    Size: Small, Type: or Medium humanoid, or back into its true form. Without wings, the fiend loses its flying speed. Other than its size and speed, its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 66,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "or Medium humanoid, or back into its true form. Without wings, the fiend loses its flying speed. Other than its size and speed, its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
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
        self.abilities.extend(['telepathic_bond'])

    def telepathic_bond(self) -> str:
        """Telepathic Bond: The fiend ignores the range restriction on its telepathy when communicating with a creature it has c..."""
        return "The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence.Shapechanger. The fiend can use"
    def telepathic_bond(self) -> str:
        """Telepathic Bond: The fiend ignores the range restriction on its telepathy when communicating with a creature it has c..."""
        return "The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence.Shapechanger. The fiend can use"

