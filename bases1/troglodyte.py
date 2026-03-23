# bases1/troglodyte.py
"""
Troglodyte creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=troglodyte
"""
from creature_base import GlobalCreatureBaseClass


class Troglodyte(GlobalCreatureBaseClass):
    """
    Troglodyte creature
    Size: Medium, Type: humanoid (Troglodyte), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Troglodyte), chaotic evil",
        "hit_points_up": [1, 1, 1],
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
        self.abilities.extend(['chameleon_skin'])

    def chameleon_skin(self) -> str:
        """Chameleon Skin: The troglodyte has advantage on Dexterity (Stealth) checks made to hide.Stench. Any creature other t..."""
        return "The troglodyte has advantage on Dexterity (Stealth) checks made to hide.Stench. Any creature other than a troglodyte that starts its turn within 5 feet of the troglodyte must succeed on a DC 12 Consti"
    def chameleon_skin(self) -> str:
        """Chameleon Skin: The troglodyte has advantage on Dexterity (Stealth) checks made to hide.Stench. Any creature other t..."""
        return "The troglodyte has advantage on Dexterity (Stealth) checks made to hide.Stench. Any creature other than a troglodyte that starts its turn within 5 feet of the troglodyte must succeed on a DC 12 Consti"

