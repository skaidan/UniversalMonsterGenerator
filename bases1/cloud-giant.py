# bases1/cloud-giant.py
"""
CloudGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cloud-giant
"""
from creature_base import GlobalCreatureBaseClass


class CloudGiant(GlobalCreatureBaseClass):
    """
    CloudGiant creature
    Size: Huge, Type: giant, neutral good (50 %) or neutral evil (50 %)
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 200,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "giant, neutral good (50 %) or neutral evil (50 %)",
        "hit_points_up": [20, 20, 20],
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
        self.abilities.extend(['keen_smell'])

    def keen_smell(self) -> str:
        """Keen Smell: The giant has advantage on Wisdom (Perception) checks that rely on smell.InnateSpellcasting. The gia..."""
        return "The giant has advantage on Wisdom (Perception) checks that rely on smell.InnateSpellcasting. The giant's innate spellcasting ability is Charisma. It can innately cast the following spells, requiring n"
    def keen_smell(self) -> str:
        """Keen Smell: The giant has advantage on Wisdom (Perception) checks that rely on smell.InnateSpellcasting. The gia..."""
        return "The giant has advantage on Wisdom (Perception) checks that rely on smell.InnateSpellcasting. The giant's innate spellcasting ability is Charisma. It can innately cast the following spells, requiring n"

