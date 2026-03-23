# bases1/cambion.py
"""
Cambion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cambion
"""
from creature_base import GlobalCreatureBaseClass


class Cambion(GlobalCreatureBaseClass):
    """
    Cambion creature
    Size: Medium, Type: fiend, any evil alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 82,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fiend, any evil alignment",
        "hit_points_up": [8, 8, 8],
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
        self.abilities.extend(['fiendish_blessing'])

    def fiendish_blessing(self) -> str:
        """Fiendish Blessing: The AC of the cambion includes its Charisma bonus.Innate Spellcasting. The cambion's spellcasting ab..."""
        return "The AC of the cambion includes its Charisma bonus.Innate Spellcasting. The cambion's spellcasting ability is Charisma (spell save DC 14). The cambion can innately cast the following spells, requiring "
    def fiendish_blessing(self) -> str:
        """Fiendish Blessing: The AC of the cambion includes its Charisma bonus.Innate Spellcasting. The cambion's spellcasting ab..."""
        return "The AC of the cambion includes its Charisma bonus.Innate Spellcasting. The cambion's spellcasting ability is Charisma (spell save DC 14). The cambion can innately cast the following spells, requiring "

