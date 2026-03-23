# bases1/vampire-spawn.py
"""
VampireSpawn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vampire-spawn
"""
from creature_base import GlobalCreatureBaseClass


class VampireSpawn(GlobalCreatureBaseClass):
    """
    VampireSpawn creature
    Size: Medium, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 82,
        "min_level": 6,
        "level": 6,
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
        "type": "undead, neutral evil",
        "hit_points_up": [8, 8, 8],
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
        self.abilities.extend(['regeneration'])

    def regeneration(self) -> str:
        """Regeneration: The vampire regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't ..."""
        return "The vampire regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the vampire takes radiant damage or damage from holy water, this tr"
    def regeneration(self) -> str:
        """Regeneration: The vampire regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't ..."""
        return "The vampire regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the vampire takes radiant damage or damage from holy water, this tr"

