# bases1/orc-hand-of-yurtrus.py
"""
OrcHandOfYurtrus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-hand-of-yurtrus
"""
from creature_base import GlobalCreatureBaseClass


class OrcHandOfYurtrus(GlobalCreatureBaseClass):
    """
    OrcHandOfYurtrus creature
    Size: Medium, Type: humanoid (Orc), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 30,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Orc), chaotic evil",
        "hit_points_up": [3, 3, 3],
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
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Spellcasting. The orc is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4"

