# bases1/clay-golem.py
"""
ClayGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=clay-golem
"""
from creature_base import GlobalCreatureBaseClass


class ClayGolem(GlobalCreatureBaseClass):
    """
    ClayGolem creature
    Size: Large, Type: construct, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 133,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "construct, unaligned",
        "hit_points_up": [13, 13, 13],
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
        self.abilities.extend(['acid_absorption'])

    def acid_absorption(self) -> str:
        """Acid Absorption: Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of h..."""
        return "Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of hit points equal to the acid damage dealt.Berserk. Whenever the golem starts its turn with 60 hit poi"
    def acid_absorption(self) -> str:
        """Acid Absorption: Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of h..."""
        return "Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of hit points equal to the acid damage dealt.Berserk. Whenever the golem starts its turn with 60 hit poi"

