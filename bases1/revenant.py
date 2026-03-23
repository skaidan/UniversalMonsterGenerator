# bases1/revenant.py
"""
Revenant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=revenant
"""
from creature_base import GlobalCreatureBaseClass


class Revenant(GlobalCreatureBaseClass):
    """
    Revenant creature
    Size: Large, Type: or smaller.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 136,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller.",
        "hit_points_up": [13, 13, 13],
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
        """Regeneration: The revenant regains 10 hit points at the start of its turn. If the revenant takes fire or radiant d..."""
        return "The revenant regains 10 hit points at the start of its turn. If the revenant takes fire or radiant damage, this trait doesn't function at the start of the revenant's next turn. The revenant's body is "
    def regeneration(self) -> str:
        """Regeneration: The revenant regains 10 hit points at the start of its turn. If the revenant takes fire or radiant d..."""
        return "The revenant regains 10 hit points at the start of its turn. If the revenant takes fire or radiant damage, this trait doesn't function at the start of the revenant's next turn. The revenant's body is "

