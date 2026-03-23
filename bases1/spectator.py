# bases1/spectator.py
"""
Spectator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spectator
"""
from creature_base import GlobalCreatureBaseClass


class Spectator(GlobalCreatureBaseClass):
    """
    Spectator creature
    Size: Medium, Type: aberration, lawful neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 39,
        "min_level": 4,
        "level": 4,
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
        "type": "aberration, lawful neutral",
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
        self.abilities.extend(['bite'])

    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) piercing damage.Eye Rays. ..."""
        return "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) piercing damage.Eye Rays. The spectator shoots up to two of the following magical eye rays at one or two creatures it can see "
    def bite(self) -> str:
        """Bite: Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) piercing damage.Eye Rays. ..."""
        return "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) piercing damage.Eye Rays. The spectator shoots up to two of the following magical eye rays at one or two creatures it can see "

