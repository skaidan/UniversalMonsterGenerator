# bases1/warlock-of-the-fiend.py
"""
WarlockOfTheFiend creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warlock-of-the-fiend
"""
from creature_base import GlobalCreatureBaseClass


class WarlockOfTheFiend(GlobalCreatureBaseClass):
    """
    WarlockOfTheFiend creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 78,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
        "hit_points_up": [7, 7, 7],
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
        self.abilities.extend(['dark_ones_own_luck_recharges_after_a_short_or_long_rest'])

    def dark_ones_own_luck_recharges_after_a_short_or_long_rest(self) -> str:
        """Dark One's Own Luck (Recharges after a Short or Long Rest): When the warlock makes an ability check or saving throw, it can add a d10 to the roll. It can do thi..."""
        return "When the warlock makes an ability check or saving throw, it can add a d10 to the roll. It can do this after the roll is made but before any of the roll's effects occur.ActionsMultiattack. The warlock "

