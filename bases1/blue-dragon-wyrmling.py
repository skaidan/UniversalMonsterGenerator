# bases1/blue-dragon-wyrmling.py
"""
BlueDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blue-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class BlueDragonWyrmling(GlobalCreatureBaseClass):
    """
    BlueDragonWyrmling creature
    Size: Medium, Type: dragon (Chromatic), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
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
        "type": "dragon (Chromatic), lawful evil",
        "hit_points_up": [5, 5, 5],
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
        """Bite: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 3 (1..."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 3 (1d6) lightning damage.Lightning Breath (Recharge 5-6). The dragon exhales lightning in a 30-foot line"
    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 3 (1..."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 3 (1d6) lightning damage.Lightning Breath (Recharge 5-6). The dragon exhales lightning in a 30-foot line"

