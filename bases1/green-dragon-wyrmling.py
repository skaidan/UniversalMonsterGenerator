# bases1/green-dragon-wyrmling.py
"""
GreenDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=green-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class GreenDragonWyrmling(GlobalCreatureBaseClass):
    """
    GreenDragonWyrmling creature
    Size: Medium, Type: dragon (Chromatic), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 38,
        "min_level": 3,
        "level": 3,
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
        "type": "dragon (Chromatic), lawful evil",
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +4 to hit, reach 5 ft., one t..."""
        return "The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 3 (1d6) poison damage.Poison Breath (Recharge 5-6). Th"
    def amphibious(self) -> str:
        """Amphibious: The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +4 to hit, reach 5 ft., one t..."""
        return "The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage plus 3 (1d6) poison damage.Poison Breath (Recharge 5-6). Th"

