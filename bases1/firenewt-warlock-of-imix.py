# bases1/firenewt-warlock-of-imix.py
"""
FirenewtWarlockOfImix creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=firenewt-warlock-of-imix
"""
from creature_base import GlobalCreatureBaseClass


class FirenewtWarlockOfImix(GlobalCreatureBaseClass):
    """
    FirenewtWarlockOfImix creature
    Size: Medium, Type: Elemental, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Elemental, typically Neutral Evil",
        "hit_points_up": [3, 3, 3],
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
        # Add creature-specific abilities
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The firenewt can breathe air and water.Devil's Sight. Magical darkness doesn't impede the firenewt's..."""
        return "The firenewt can breathe air and water.Devil's Sight. Magical darkness doesn't impede the firenewt's darkvision.Imix's Blessing. When the firenewt reduces an enemy to 0 hit points, the firenewt gains "

