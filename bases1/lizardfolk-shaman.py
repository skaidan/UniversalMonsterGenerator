# bases1/lizardfolk-shaman.py
"""
LizardfolkShaman creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lizardfolk-shaman
"""
from creature_base import GlobalCreatureBaseClass


class LizardfolkShaman(GlobalCreatureBaseClass):
    """
    LizardfolkShaman creature
    Size: Large, Type: or smaller creature, the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the lizardfolk can't bite another target. If the lizardfolk reverts to its true form, the grapple ends.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 27,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller creature, the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the lizardfolk can't bite another target. If the lizardfolk reverts to its true form, the grapple ends.",
        "hit_points_up": [2, 2, 2],
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
        """Hold Breath: The lizardfolk can hold its breath for 15 minutes.Spellcasting (Lizardfolk Form Only). The lizardfol..."""
        return "The lizardfolk can hold its breath for 15 minutes.Spellcasting (Lizardfolk Form Only). The lizardfolk is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with s"
    def hold_breath(self) -> str:
        """Hold Breath: The lizardfolk can hold its breath for 15 minutes.Spellcasting (Lizardfolk Form Only). The lizardfol..."""
        return "The lizardfolk can hold its breath for 15 minutes.Spellcasting (Lizardfolk Form Only). The lizardfolk is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with s"

