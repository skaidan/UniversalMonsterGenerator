# bases1/drow-inquisitor.py
"""
DrowInquisitor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-inquisitor
"""
from creature_base import GlobalCreatureBaseClass


class DrowInquisitor(GlobalCreatureBaseClass):
    """
    DrowInquisitor creature
    Size: Medium, Type: Humanoid (Cleric, Elf), typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 149,
        "min_level": 15,
        "level": 15,
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
        "type": "Humanoid (Cleric, Elf), typically Neutral Evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['discern_lie'])

    def discern_lie(self) -> str:
        """Discern Lie: The drow discerns when a creature in earshot speaks a lie in a language the drow knows.Fey Ancestry...."""
        return "The drow discerns when a creature in earshot speaks a lie in a language the drow knows.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to slee"

