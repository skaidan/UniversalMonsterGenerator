# bases1/quetzalcoatlus.py
"""
Quetzalcoatlus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quetzalcoatlus
"""
from creature_base import GlobalCreatureBaseClass


class Quetzalcoatlus(GlobalCreatureBaseClass):
    """
    Quetzalcoatlus creature
    Size: Huge, Type: Beast (Dinosaur), unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 30,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Beast (Dinosaur), unaligned",
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
        # Add creature-specific abilities
        self.abilities.extend(['flyby'])

    def flyby(self) -> str:
        """Flyby: The quetzalcoatlus doesn't provoke an opportunity attack when it flies out of an enemy's reach.Actio..."""
        return "The quetzalcoatlus doesn't provoke an opportunity attack when it flies out of an enemy's reach.ActionsBite. Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit: 12 (3d6 + 2) piercing damag"

