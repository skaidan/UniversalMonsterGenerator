# bases1/orc-claw-of-luthic.py
"""
OrcClawOfLuthic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-claw-of-luthic
"""
from creature_base import GlobalCreatureBaseClass


class OrcClawOfLuthic(GlobalCreatureBaseClass):
    """
    OrcClawOfLuthic creature
    Size: Medium, Type: humanoid (Orc), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Orc), chaotic evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['aggressive'])

    def aggressive(self) -> str:
        """Aggressive: As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Spellc..."""
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Spellcasting. The orc is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4"

