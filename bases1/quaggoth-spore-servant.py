# bases1/quaggoth-spore-servant.py
"""
QuaggothSporeServant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quaggoth-spore-servant
"""
from creature_base import GlobalCreatureBaseClass


class QuaggothSporeServant(GlobalCreatureBaseClass):
    """
    QuaggothSporeServant creature
    Size: Medium, Type: plant, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
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
        "size": "Medium",
        "type": "plant, unaligned",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The spore servant makes two claw attacks.Claw. Melee Weapon Attack: +5 to hit, reach 5 ft., one targ..."""
        return "The spore servant makes two claw attacks.Claw. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.Monster Manual
			
				
			    	DnD 5e Monsters › Quaggoth Spor"
    def multiattack(self) -> str:
        """Multiattack: The spore servant makes two claw attacks.Claw. Melee Weapon Attack: +5 to hit, reach 5 ft., one targ..."""
        return "The spore servant makes two claw attacks.Claw. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.Monster Manual
			
				
			    	DnD 5e Monsters › Quaggoth Spor"

