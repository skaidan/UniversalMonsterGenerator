# bases1/archdruid.py
"""
Archdruid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=archdruid
"""
from creature_base import GlobalCreatureBaseClass


class Archdruid(GlobalCreatureBaseClass):
    """
    Archdruid creature
    Size: Medium, Type: Humanoid (Druid), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 154,
        "min_level": 13,
        "level": 13,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid (Druid), any alignment",
        "hit_points_up": [15, 15, 15],
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
        """Multiattack: The archdruid makes three Staff or Wildfire attacks. It can replace one attack with a use of Spellca..."""
        return "The archdruid makes three Staff or Wildfire attacks. It can replace one attack with a use of Spellcasting.Staff. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning d"

