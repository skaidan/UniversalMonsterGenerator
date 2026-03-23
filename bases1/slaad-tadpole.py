# bases1/slaad-tadpole.py
"""
SlaadTadpole creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=slaad-tadpole
"""
from creature_base import GlobalCreatureBaseClass


class SlaadTadpole(GlobalCreatureBaseClass):
    """
    SlaadTadpole creature
    Size: Tiny, Type: aberration, chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 10,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "aberration, chaotic neutral",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The slaad has Advantage on saving throws against spells and other magical effects.ActionsBite. Melee..."""
        return "The slaad has Advantage on saving throws against spells and other magical effects.ActionsBite. Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage.Monster Manual
			
				
			    	DnD 5"
    def magic_resistance(self) -> str:
        """Magic Resistance: The slaad has Advantage on saving throws against spells and other magical effects.ActionsBite. Melee..."""
        return "The slaad has Advantage on saving throws against spells and other magical effects.ActionsBite. Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage.Monster Manual
			
				
			    	DnD 5"

