# bases1/red-dragon-wyrmling.py
"""
RedDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=red-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class RedDragonWyrmling(GlobalCreatureBaseClass):
    """
    RedDragonWyrmling creature
    Size: Medium, Type: dragon (Chromatic), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 75,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "dragon (Chromatic), chaotic evil",
        "hit_points_up": [7, 7, 7],
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
        """Bite: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage plus 3 (1..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage plus 3 (1d6) fire damage.Fire Breath (Recharge 5-6). The dragon exhales fire in a 15-foot cone. Each creature"
    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage plus 3 (1..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage plus 3 (1d6) fire damage.Fire Breath (Recharge 5-6). The dragon exhales fire in a 15-foot cone. Each creature"

