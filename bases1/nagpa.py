# bases1/nagpa.py
"""
Nagpa creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nagpa
"""
from creature_base import GlobalCreatureBaseClass


class Nagpa(GlobalCreatureBaseClass):
    """
    Nagpa creature
    Size: Medium, Type: Monstrosity (Wizard), typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 203,
        "min_level": 18,
        "level": 18,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Monstrosity (Wizard), typically Neutral Evil",
        "hit_points_up": [20, 20, 20],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The nagpa makes three Staff or Deathly Ray attacks. It can replace one attack with a use of Spellcas..."""
        return "The nagpa makes three Staff or Deathly Ray attacks. It can replace one attack with a use of Spellcasting.Staff. Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning da"

