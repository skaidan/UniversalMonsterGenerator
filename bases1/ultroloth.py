# bases1/ultroloth.py
"""
Ultroloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ultroloth
"""
from creature_base import GlobalCreatureBaseClass


class Ultroloth(GlobalCreatureBaseClass):
    """
    Ultroloth creature
    Size: Medium, Type: fiend (Yugoloth), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 153,
        "min_level": 14,
        "level": 14,
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
        "type": "fiend (Yugoloth), neutral evil",
        "hit_points_up": [15, 15, 15],
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
        """Innate Spellcasting: The ultroloth's innate spellcasting ability is Charisma (spell save DC 17). The ultroloth can innate..."""
        return "The ultroloth's innate spellcasting ability is Charisma (spell save DC 17). The ultroloth can innately cast the following spells, requiring no material components:At will: alter self, clairvoyance, da"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The ultroloth's innate spellcasting ability is Charisma (spell save DC 17). The ultroloth can innate..."""
        return "The ultroloth's innate spellcasting ability is Charisma (spell save DC 17). The ultroloth can innately cast the following spells, requiring no material components:At will: alter self, clairvoyance, da"

