# bases1/badger.py
"""
Badger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=badger
"""
from creature_base import GlobalCreatureBaseClass


class Badger(GlobalCreatureBaseClass):
    """
    Tiny Beast creature - Badger
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 3,
        "min_level": 1,
        "level": 1,
        "STR": 4,
        "DEX": 11,
        "CON": 12,
        "INT": 2,
        "WIS": 12,
        "CHAR": 5,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "Beast",
        "hit_points_up": [1, 1, 1],
        "STR_up": [1, 1, 0],
        "DEX_up": [0, 1, 0],
        "CON_up": [0, 0, 1],
        "INT_up": [1, 0, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 0],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.extend(['keen_smell'])
        self.abilities.append("Bite")

    def keen_smell(self) -> str:
        """The badger has advantage on Wisdom (Perception) checks that rely on smell."""
        return "Advantage on Wisdom (Perception) checks that rely on smell"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage"

    def speed_description(self) -> str:
        """Speed: 20 ft., burrow 5 ft."""
        return "20 ft., burrow 5 ft."

    def senses_description(self) -> str:
        """Senses: darkvision 30 ft., passive Perception 11"""
        return "Darkvision 30 ft., passive Perception 11"
    def keen_smell(self) -> str:
        """Keen Smell: The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsBite. Melee Weapon ..."""
        return "The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsBite. Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage.Monster Manual (SRD)
			
				
			"
    def keen_smell(self) -> str:
        """Keen Smell: The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsBite. Melee Weapon ..."""
        return "The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsBite. Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage.Monster Manual (SRD)
			
				
			"

