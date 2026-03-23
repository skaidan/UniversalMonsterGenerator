# bases1/yuan-ti-pureblood.py
"""
YuanTiPureblood creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-pureblood
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiPureblood(GlobalCreatureBaseClass):
    """
    YuanTiPureblood creature
    Size: Medium, Type: humanoid (Yuan-ti), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 40,
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
        "type": "humanoid (Yuan-ti), neutral evil",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['innate_spellcasting'])

    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The yuan-ti's spellcasting ability is Charisma (spell save DC 12). The yuan-ti can innately cast the..."""
        return "The yuan-ti's spellcasting ability is Charisma (spell save DC 12). The yuan-ti can innately cast the following spells, requiring no material components:At will: animal friendship (snakes only)3/day ea"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The yuan-ti's spellcasting ability is Charisma (spell save DC 12). The yuan-ti can innately cast the..."""
        return "The yuan-ti's spellcasting ability is Charisma (spell save DC 12). The yuan-ti can innately cast the following spells, requiring no material components:At will: animal friendship (snakes only)3/day ea"

