# bases1/nycaloth.py
"""
Nycaloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nycaloth
"""
from creature_base import GlobalCreatureBaseClass


class Nycaloth(GlobalCreatureBaseClass):
    """
    Nycaloth creature
    Size: Large, Type: fiend (Yugoloth), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 123,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend (Yugoloth), neutral evil",
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
        self.abilities.extend(['innate_spellcasting'])

    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The nycaloth's innate spellcasting ability is Charisma. The nycaloth can innately cast the following..."""
        return "The nycaloth's innate spellcasting ability is Charisma. The nycaloth can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel magic, invisibilit"
    def innate_spellcasting(self) -> str:
        """Innate Spellcasting: The nycaloth's innate spellcasting ability is Charisma. The nycaloth can innately cast the following..."""
        return "The nycaloth's innate spellcasting ability is Charisma. The nycaloth can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel magic, invisibilit"

