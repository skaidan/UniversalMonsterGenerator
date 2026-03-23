# bases1/aarakocra.py
"""
Aarakocra creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=aarakocra
"""
from creature_base import GlobalCreatureBaseClass


class Aarakocra(GlobalCreatureBaseClass):
    """
    Aarakocra creature
    Size: Medium, Type: humanoid (Aarakocra), neutral good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Aarakocra), neutral good",
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
        self.abilities.extend(['dive_attack'])

    def dive_attack(self) -> str:
        """Dive Attack: If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with..."""
        return "If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target.ActionsTalon. Melee W"
    def dive_attack(self) -> str:
        """Dive Attack: If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with..."""
        return "If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target.ActionsTalon. Melee W"

