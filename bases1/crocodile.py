# bases1/crocodile.py
"""
Crocodile creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crocodile
"""
from creature_base import GlobalCreatureBaseClass


class Crocodile(GlobalCreatureBaseClass):
    """
    Crocodile creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 19,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The crocodile can hold its breath for 15 minutes.ActionsBite. Melee Weapon Attack: +4 to hit, reach ..."""
        return "The crocodile can hold its breath for 15 minutes.ActionsBite. Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target is grappled (escape DC 12). U"
    def hold_breath(self) -> str:
        """Hold Breath: The crocodile can hold its breath for 15 minutes.ActionsBite. Melee Weapon Attack: +4 to hit, reach ..."""
        return "The crocodile can hold its breath for 15 minutes.ActionsBite. Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target is grappled (escape DC 12). U"

