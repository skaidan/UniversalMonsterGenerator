# bases1/noble.py
"""
Noble creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=noble
"""
from creature_base import GlobalCreatureBaseClass


class Noble(GlobalCreatureBaseClass):
    """
    Noble creature
    Size: Medium, Type: humanoid (any race), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 9,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), any alignment",
        "hit_points_up": [1, 1, 1],
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
        self.abilities.extend(['rapier'])

    def rapier(self) -> str:
        """Rapier: Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.ReactionsP..."""
        return "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.ReactionsParry. The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble mus"
    def rapier(self) -> str:
        """Rapier: Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.ReactionsP..."""
        return "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.ReactionsParry. The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble mus"

