# bases1/commoner.py
"""
Commoner creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=commoner
"""
from creature_base import GlobalCreatureBaseClass


class Commoner(GlobalCreatureBaseClass):
    """
    Commoner creature
    Size: Medium, Type: humanoid (any race), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 4,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), any alignment",
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
        self.abilities.extend(['club'])

    def club(self) -> str:
        """Club: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Commoners i..."""
        return "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Commoners include peasants, serfs, slaves, servants, pilgrims, merchants, artisans, and hermits.Monster Manual "
    def club(self) -> str:
        """Club: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Commoners i..."""
        return "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Commoners include peasants, serfs, slaves, servants, pilgrims, merchants, artisans, and hermits.Monster Manual "

