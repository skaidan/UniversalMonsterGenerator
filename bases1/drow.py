# bases1/drow.py
"""
Drow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow
"""
from creature_base import GlobalCreatureBaseClass


class Drow(GlobalCreatureBaseClass):
    """
    Drow creature
    Size: Medium, Type: humanoid (Elf), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Elf), neutral evil",
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
        self.abilities.extend(['fey_ancestry'])

    def fey_ancestry(self) -> str:
        """Fey Ancestry: The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep..."""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's spellcasting ability is Charisma (spell save DC 11). It can innatel"
    def fey_ancestry(self) -> str:
        """Fey Ancestry: The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep..."""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's spellcasting ability is Charisma (spell save DC 11). It can innatel"

