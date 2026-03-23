# bases1/djinni.py
"""
Djinni creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=djinni
"""
from creature_base import GlobalCreatureBaseClass


class Djinni(GlobalCreatureBaseClass):
    """
    Djinni creature
    Size: Large, Type: elemental, chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 161,
        "min_level": 12,
        "level": 12,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "elemental, chaotic good",
        "hit_points_up": [16, 16, 16],
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
        self.abilities.extend(['elemental_demise'])

    def elemental_demise(self) -> str:
        """Elemental Demise: If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the dji..."""
        return "If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the djinni was wearing or carrying.Innate Spellcasting. The djinni's innate spellcasting ability is Charism"
    def elemental_demise(self) -> str:
        """Elemental Demise: If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the dji..."""
        return "If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the djinni was wearing or carrying.Innate Spellcasting. The djinni's innate spellcasting ability is Charism"

