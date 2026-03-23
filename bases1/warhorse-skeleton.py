# bases1/warhorse-skeleton.py
"""
WarhorseSkeleton creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warhorse-skeleton
"""
from creature_base import GlobalCreatureBaseClass


class WarhorseSkeleton(GlobalCreatureBaseClass):
    """
    WarhorseSkeleton creature
    Size: Large, Type: undead, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
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
        "type": "undead, lawful evil",
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
        self.abilities.extend(['hooves'])

    def hooves(self) -> str:
        """Hooves: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.Monste..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Warhorse Skeleton"
    def hooves(self) -> str:
        """Hooves: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.Monste..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Warhorse Skeleton"

