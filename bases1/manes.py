# bases1/manes.py
"""
Manes creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=manes
"""
from creature_base import GlobalCreatureBaseClass


class Manes(GlobalCreatureBaseClass):
    """
    Manes creature
    Size: Small, Type: fiend (Demon), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 9,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 9,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "fiend (Demon), chaotic evil",
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
        self.abilities.extend(['claws'])

    def claws(self) -> str:
        """Claws: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.Monster Manual..."""
        return "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.Monster Manual
			
				
			    	DnD 5e Monsters › Manes"
    def claws(self) -> str:
        """Claws: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.Monster Manual..."""
        return "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.Monster Manual
			
				
			    	DnD 5e Monsters › Manes"

