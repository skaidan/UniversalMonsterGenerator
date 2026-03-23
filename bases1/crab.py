# bases1/crab.py
"""
Crab creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crab
"""
from creature_base import GlobalCreatureBaseClass


class Crab(GlobalCreatureBaseClass):
    """
    Crab creature
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
        "armor_class": 11,
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +0 to hit, reach 5 ft., one tar..."""
        return "The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Crab"
    def amphibious(self) -> str:
        """Amphibious: The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +0 to hit, reach 5 ft., one tar..."""
        return "The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Crab"

