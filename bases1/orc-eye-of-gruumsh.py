# bases1/orc-eye-of-gruumsh.py
"""
OrcEyeOfGruumsh creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-eye-of-gruumsh
"""
from creature_base import GlobalCreatureBaseClass


class OrcEyeOfGruumsh(GlobalCreatureBaseClass):
    """
    OrcEyeOfGruumsh creature
    Size: Medium, Type: humanoid (Orc), chaotic evil
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
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Orc), chaotic evil",
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
        self.abilities.extend(['aggressive'])

    def aggressive(self) -> str:
        """Aggressive: As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruums..."""
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruumsh's Fury. The orc deals an extra 4 (1d8) damage when it hits with a weapon attack (included in the a"
    def aggressive(self) -> str:
        """Aggressive: As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruums..."""
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Gruumsh's Fury. The orc deals an extra 4 (1d8) damage when it hits with a weapon attack (included in the a"

