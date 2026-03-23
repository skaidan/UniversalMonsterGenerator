# bases1/drider.py
"""
Drider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drider
"""
from creature_base import GlobalCreatureBaseClass


class Drider(GlobalCreatureBaseClass):
    """
    Drider creature
    Size: Large, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 123,
        "min_level": 7,
        "level": 7,
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
        "type": "monstrosity, chaotic evil",
        "hit_points_up": [12, 12, 12],
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
        self.abilities.extend(['fey_ancestry'])

    def fey_ancestry(self) -> str:
        """Fey Ancestry: The drider has advantage on saving throws against being charmed, and magic can't put the drider to s..."""
        return "The drider has advantage on saving throws against being charmed, and magic can't put the drider to sleep.Innate Spellcasting. The drider's innate spellcasting ability is Wisdom (spell save DC 13). The"
    def fey_ancestry(self) -> str:
        """Fey Ancestry: The drider has advantage on saving throws against being charmed, and magic can't put the drider to s..."""
        return "The drider has advantage on saving throws against being charmed, and magic can't put the drider to sleep.Innate Spellcasting. The drider's innate spellcasting ability is Wisdom (spell save DC 13). The"

