# bases1/androsphinx.py
"""
Androsphinx creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=androsphinx
"""
from creature_base import GlobalCreatureBaseClass


class Androsphinx(GlobalCreatureBaseClass):
    """
    Androsphinx creature
    Size: Large, Type: monstrosity, lawful neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 199,
        "min_level": 18,
        "level": 18,
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
        "type": "monstrosity, lawful neutral",
        "hit_points_up": [19, 19, 19],
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
        self.abilities.extend(['inscrutable'])

    def inscrutable(self) -> str:
        """Inscrutable: The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as an..."""
        return "The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intention"
    def inscrutable(self) -> str:
        """Inscrutable: The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as an..."""
        return "The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intention"

