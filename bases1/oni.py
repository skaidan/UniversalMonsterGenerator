# bases1/oni.py
"""
Oni creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=oni
"""
from creature_base import GlobalCreatureBaseClass


class Oni(GlobalCreatureBaseClass):
    """
    Oni creature
    Size: Small, Type: or Medium humanoid, into a Large giant, or back into its true form. Other than its size, its statistics are the same in each form. The only equipment that is transformed is its glaive, which shrinks so that it can be wielded in humanoid form. If the oni dies, it reverts to its true form, and its glaive reverts to its normal size.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 110,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "or Medium humanoid, into a Large giant, or back into its true form. Other than its size, its statistics are the same in each form. The only equipment that is transformed is its glaive, which shrinks so that it can be wielded in humanoid form. If the oni dies, it reverts to its true form, and its glaive reverts to its normal size.",
        "hit_points_up": [11, 11, 11],
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
        """Innate Spellcasting: The oni's innate spellcasting ability is Charisma (spell save DC 13). The oni can innately cast the ..."""
        return "The oni's innate spellcasting ability is Charisma (spell save DC 13). The oni can innately cast the following spells, requiring no material components:At will: darkness, invisibility1/day each: charm "
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The oni's innate spellcasting ability is Charisma (spell save DC 13). The oni can innately cast the ..."""
        return "The oni's innate spellcasting ability is Charisma (spell save DC 13). The oni can innately cast the following spells, requiring no material components:At will: darkness, invisibility1/day each: charm "

