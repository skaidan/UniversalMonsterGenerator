# bases1/annis-hag.py
"""
AnnisHag creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=annis-hag
"""
from creature_base import GlobalCreatureBaseClass


class AnnisHag(GlobalCreatureBaseClass):
    """
    AnnisHag creature
    Size: Medium, Type: Humanoid),
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 90,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid),",
        "hit_points_up": [9, 9, 9],
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
        """Multiattack: The annis makes one Bite attack and two Claw attacks.Bite. Melee Weapon Attack: +8 to hit, reach 5 f..."""
        return "The annis makes one Bite attack and two Claw attacks.Bite. Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 5) piercing damage.Claw. Melee Weapon Attack: +8 to hit, reach 5 ft.,"

