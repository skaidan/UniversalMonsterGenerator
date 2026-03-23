# bases1/silver-dragon-wyrmling.py
"""
SilverDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=silver-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class SilverDragonWyrmling(GlobalCreatureBaseClass):
    """
    SilverDragonWyrmling creature
    Size: Medium, Type: dragon (Metallic), lawful good
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
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "dragon (Metallic), lawful good",
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
        self.abilities.extend(['bite'])

    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage.Breath We..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage.Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.Cold Breath. The dragon ex"
    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage.Breath We..."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage.Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.Cold Breath. The dragon ex"

