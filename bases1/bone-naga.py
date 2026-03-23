# bases1/bone-naga.py
"""
BoneNaga creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bone-naga
"""
from creature_base import GlobalCreatureBaseClass


class BoneNaga(GlobalCreatureBaseClass):
    """
    BoneNaga creature
    Size: Large, Type: undead, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 58,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "undead, lawful evil",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['spellcasting'])

    def spellcasting(self) -> str:
        """Spellcasting: The naga is a 5th-level spellcaster (spell save DC 12, +4 to hit with spell attacks) that needs only..."""
        return "The naga is a 5th-level spellcaster (spell save DC 12, +4 to hit with spell attacks) that needs only verbal components to cast its spells.If the naga was a guardian naga in life, its spellcasting abil"
    def spellcasting(self) -> str:
        """Spellcasting: The naga is a 5th-level spellcaster (spell save DC 12, +4 to hit with spell attacks) that needs only..."""
        return "The naga is a 5th-level spellcaster (spell save DC 12, +4 to hit with spell attacks) that needs only verbal components to cast its spells.If the naga was a guardian naga in life, its spellcasting abil"

