# bases1/githyanki-warrior.py
"""
GithyankiWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githyanki-warrior
"""
from creature_base import GlobalCreatureBaseClass


class GithyankiWarrior(GlobalCreatureBaseClass):
    """
    GithyankiWarrior creature
    Size: Medium, Type: humanoid (Gith), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 49,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Gith), lawful evil",
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
        self.abilities.extend(['innate_spellcasting_psionics'])

    def innate_spellcasting_psionics(self) -> str:
        """Innate Spellcasting (Psionics): The githyanki's innate spellcasting ability is Intelligence. It can innately cast the following spel..."""
        return "The githyanki's innate spellcasting ability is Intelligence. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: jump, misty step, "
    def innate_spellcasting_psionics(self) -> str:
        """Innate Spellcasting (Psionics): The githyanki's innate spellcasting ability is Intelligence. It can innately cast the following spel..."""
        return "The githyanki's innate spellcasting ability is Intelligence. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: jump, misty step, "

