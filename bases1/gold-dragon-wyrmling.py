# bases1/gold-dragon-wyrmling.py
"""
GoldDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gold-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class GoldDragonWyrmling(GlobalCreatureBaseClass):
    """
    GoldDragonWyrmling creature
    Size: Medium, Type: dragon (Metallic), lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 60,
        "min_level": 4,
        "level": 4,
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
        "type": "dragon (Metallic), lawful good",
        "hit_points_up": [6, 6, 6],
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
        """Amphibious: The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +6 to hit, reach 5 ft., one t..."""
        return "The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage.Breath Weapons (Recharge 5-6). The dragon uses one of the f"
    def amphibious(self) -> str:
        """Amphibious: The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +6 to hit, reach 5 ft., one t..."""
        return "The dragon can breathe air and water.ActionsBite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage.Breath Weapons (Recharge 5-6). The dragon uses one of the f"

