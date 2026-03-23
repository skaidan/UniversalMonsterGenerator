# bases1/merfolk.py
"""
Merfolk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merfolk
"""
from creature_base import GlobalCreatureBaseClass


class Merfolk(GlobalCreatureBaseClass):
    """
    Merfolk creature
    Size: Medium, Type: humanoid (Merfolk), neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Merfolk), neutral",
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The merfolk can breathe air and water.ActionsSpear. Melee or Ranged Weapon Attack: +2 to hit, reach ..."""
        return "The merfolk can breathe air and water.ActionsSpear. Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 3 (1d6) piercing damage, or 4 (1d8) piercing damage if us"
    def amphibious(self) -> str:
        """Amphibious: The merfolk can breathe air and water.ActionsSpear. Melee or Ranged Weapon Attack: +2 to hit, reach ..."""
        return "The merfolk can breathe air and water.ActionsSpear. Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 3 (1d6) piercing damage, or 4 (1d8) piercing damage if us"

