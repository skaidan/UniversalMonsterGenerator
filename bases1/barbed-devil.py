# bases1/barbed-devil.py
"""
BarbedDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=barbed-devil
"""
from creature_base import GlobalCreatureBaseClass


class BarbedDevil(GlobalCreatureBaseClass):
    """
    BarbedDevil creature
    Size: Medium, Type: fiend (Devil), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 110,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fiend (Devil), lawful evil",
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
        self.abilities.extend(['barbed_hide'])

    def barbed_hide(self) -> str:
        """Barbed Hide: At the start of each of its turns, the barbed devil deals 5 (1d10) piercing damage to any creature g..."""
        return "At the start of each of its turns, the barbed devil deals 5 (1d10) piercing damage to any creature grappling it.Devil's Sight. Magical darkness doesn't impede the devil's darkvision.Magic Resistance. "
    def barbed_hide(self) -> str:
        """Barbed Hide: At the start of each of its turns, the barbed devil deals 5 (1d10) piercing damage to any creature g..."""
        return "At the start of each of its turns, the barbed devil deals 5 (1d10) piercing damage to any creature grappling it.Devil's Sight. Magical darkness doesn't impede the devil's darkvision.Magic Resistance. "

