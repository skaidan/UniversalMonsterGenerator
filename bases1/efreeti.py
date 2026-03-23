# bases1/efreeti.py
"""
Efreeti creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=efreeti
"""
from creature_base import GlobalCreatureBaseClass


class Efreeti(GlobalCreatureBaseClass):
    """
    Efreeti creature
    Size: Large, Type: elemental, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 200,
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
        "type": "elemental, lawful evil",
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
        self.abilities.extend(['elemental_demise'])

    def elemental_demise(self) -> str:
        """Elemental Demise: If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind onl..."""
        return "If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment the efreeti was wearing or carrying.Innate Spellcasting. The efreeti's innate spellcasti"
    def elemental_demise(self) -> str:
        """Elemental Demise: If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind onl..."""
        return "If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment the efreeti was wearing or carrying.Innate Spellcasting. The efreeti's innate spellcasti"

