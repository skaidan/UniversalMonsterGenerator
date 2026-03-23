# bases1/draft-horse.py
"""
DraftHorse creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draft-horse
"""
from creature_base import GlobalCreatureBaseClass


class DraftHorse(GlobalCreatureBaseClass):
    """
    DraftHorse creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 19,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
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
        self.abilities.extend(['hooves'])

    def hooves(self) -> str:
        """Hooves: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.Monster..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Draft Horse"
    def hooves(self) -> str:
        """Hooves: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.Monster..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Draft Horse"

