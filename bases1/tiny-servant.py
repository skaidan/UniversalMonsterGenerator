# bases1/tiny-servant.py
"""
TinyServant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tiny-servant
"""
from creature_base import GlobalCreatureBaseClass


class TinyServant(GlobalCreatureBaseClass):
    """
    TinyServant creature
    Size: Tiny, Type: Servant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 10,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "Servant",
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
        # Add creature-specific abilities
        self.abilities.extend(['slam'])

    def slam(self) -> str:
        """Slam: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage.See the..."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage.See the tiny servant spell.Rules (Xanathar´s Guide to Everything)
			
				
			    	DnD 5e Monsters › Tiny S"

