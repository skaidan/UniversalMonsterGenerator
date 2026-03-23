# bases1/wererat.py
"""
Wererat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wererat
"""
from creature_base import GlobalCreatureBaseClass


class Wererat(GlobalCreatureBaseClass):
    """
    Wererat creature
    Size: Medium, Type: humanoid (Human, Shapechanger), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
        "min_level": 3,
        "level": 3,
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
        "type": "humanoid (Human, Shapechanger), lawful evil",
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
        self.abilities.extend(['shapechanger'])

    def shapechanger(self) -> str:
        """Shapechanger: The wererat can use its action to polymorph into a rat-humanoid hybrid or into a giant rat, or back ..."""
        return "The wererat can use its action to polymorph into a rat-humanoid hybrid or into a giant rat, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for"
    def shapechanger(self) -> str:
        """Shapechanger: The wererat can use its action to polymorph into a rat-humanoid hybrid or into a giant rat, or back ..."""
        return "The wererat can use its action to polymorph into a rat-humanoid hybrid or into a giant rat, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for"

