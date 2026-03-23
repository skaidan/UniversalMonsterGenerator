# bases1/ankylosaurus.py
"""
Ankylosaurus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ankylosaurus
"""
from creature_base import GlobalCreatureBaseClass


class Ankylosaurus(GlobalCreatureBaseClass):
    """
    Ankylosaurus creature
    Size: Huge, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 68,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast, unaligned",
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
        self.abilities.extend(['tail'])

    def tail(self) -> str:
        """Tail: Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 18 (4d6 + 4) bludgeoning damage. If t..."""
        return "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 18 (4d6 + 4) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone.Thick "
    def tail(self) -> str:
        """Tail: Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 18 (4d6 + 4) bludgeoning damage. If t..."""
        return "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 18 (4d6 + 4) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone.Thick "

