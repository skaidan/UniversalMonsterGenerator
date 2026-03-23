# bases1/copper-dragon-wyrmling.py
"""
CopperDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=copper-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class CopperDragonWyrmling(GlobalCreatureBaseClass):
    """
    CopperDragonWyrmling creature
    Size: Medium, Type: dragon (Metallic), chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "dragon (Metallic), chaotic good",
        "hit_points_up": [2, 2, 2],
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
        """Bite: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage.Breath We..."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage.Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.Acid Breath. The dragon ex"
    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage.Breath We..."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage.Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.Acid Breath. The dragon ex"

