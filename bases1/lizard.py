# bases1/lizard.py
"""
Lizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lizard
"""
from creature_base import GlobalCreatureBaseClass


class Lizard(GlobalCreatureBaseClass):
    """
    Lizard creature
    Size: Tiny, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 2,
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
        "size": "Tiny",
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
        self.abilities.extend(['bite'])

    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage.Monster Manual (SRD)..."""
        return "Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Lizard"
    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage.Monster Manual (SRD)..."""
        return "Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Lizard"

