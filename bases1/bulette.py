# bases1/bulette.py
"""
Bulette creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bulette
"""
from creature_base import GlobalCreatureBaseClass


class Bulette(GlobalCreatureBaseClass):
    """
    Bulette creature
    Size: Large, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 94,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, unaligned",
        "hit_points_up": [9, 9, 9],
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
        self.abilities.extend(['standing_leap'])

    def standing_leap(self) -> str:
        """Standing Leap: The bulette's long jump is up to 30 feet and its high jump is up to 15 feet, with or without a runni..."""
        return "The bulette's long jump is up to 30 feet and its high jump is up to 15 feet, with or without a running start.ActionsBite. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 30 (4d12 + 4) pi"
    def standing_leap(self) -> str:
        """Standing Leap: The bulette's long jump is up to 30 feet and its high jump is up to 15 feet, with or without a runni..."""
        return "The bulette's long jump is up to 30 feet and its high jump is up to 15 feet, with or without a running start.ActionsBite. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 30 (4d12 + 4) pi"

