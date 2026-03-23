# bases1/war-priest.py
"""
WarPriest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=war-priest
"""
from creature_base import GlobalCreatureBaseClass


class WarPriest(GlobalCreatureBaseClass):
    """
    WarPriest creature
    Size: Medium, Type: Humanoid (Cleric), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 117,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid (Cleric), any alignment",
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
        # Add creature-specific abilities
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The war priest makes two Maul attacks, and it uses Holy Fire.Maul. Melee Weapon Attack: +7 to hit, r..."""
        return "The war priest makes two Maul attacks, and it uses Holy Fire.Maul. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) radiant damage.Holy Fire."

