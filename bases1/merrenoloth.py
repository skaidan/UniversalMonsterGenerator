# bases1/merrenoloth.py
"""
Merrenoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merrenoloth
"""
from creature_base import GlobalCreatureBaseClass


class Merrenoloth(GlobalCreatureBaseClass):
    """
    Merrenoloth creature
    Size: Medium, Type: Fiend (Yugoloth), typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 40,
        "min_level": 4,
        "level": 4,
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
        "type": "Fiend (Yugoloth), typically Neutral Evil",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The merrenoloth has advantage on saving throws against spells and other magical effects.ActionsMulti..."""
        return "The merrenoloth has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The merrenoloth makes one Oar attack and uses Fear Gaze.Oar. Melee Weapon Attack: +5 to hit,"

