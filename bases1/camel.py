# bases1/camel.py
"""
Camel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=camel
"""
from creature_base import GlobalCreatureBaseClass


class Camel(GlobalCreatureBaseClass):
    """
    Camel creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 15,
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
        self.abilities.extend(['bite'])

    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Monster Man..."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Camel"
    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Monster Man..."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Camel"

