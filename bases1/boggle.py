# bases1/boggle.py
"""
Boggle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=boggle
"""
from creature_base import GlobalCreatureBaseClass


class Boggle(GlobalCreatureBaseClass):
    """
    Boggle creature
    Size: Tiny, Type: creature without squeezing.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 18,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "creature without squeezing.",
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
        # Add creature-specific abilities
        self.abilities.extend(['pummel'])

    def pummel(self) -> str:
        """Pummel: Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage.Oil Pud..."""
        return "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage.Oil Puddle. The boggle creates a puddle of nonflammable oil. The puddle is 1 inch deep and covers the groun"

