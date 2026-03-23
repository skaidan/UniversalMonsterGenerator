# bases1/rust-monster.py
"""
RustMonster creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rust-monster
"""
from creature_base import GlobalCreatureBaseClass


class RustMonster(GlobalCreatureBaseClass):
    """
    RustMonster creature
    Size: Medium, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 27,
        "min_level": 2,
        "level": 2,
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
        "type": "monstrosity, unaligned",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['iron_scent'])

    def iron_scent(self) -> str:
        """Iron Scent: The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it.Rust Met..."""
        return "The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it.Rust Metal. Any nonmagical weapon made of metal that hits the rust monster corrodes. After dealing damage, t"
    def iron_scent(self) -> str:
        """Iron Scent: The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it.Rust Met..."""
        return "The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it.Rust Metal. Any nonmagical weapon made of metal that hits the rust monster corrodes. After dealing damage, t"

