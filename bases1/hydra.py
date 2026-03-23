# bases1/hydra.py
"""
Hydra creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hydra
"""
from creature_base import GlobalCreatureBaseClass


class Hydra(GlobalCreatureBaseClass):
    """
    Hydra creature
    Size: Huge, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 172,
        "min_level": 9,
        "level": 9,
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
        "type": "monstrosity, unaligned",
        "hit_points_up": [17, 17, 17],
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The hydra can hold its breath for 1 hour.Multiple Heads. The hydra has five heads. While it has more..."""
        return "The hydra can hold its breath for 1 hour.Multiple Heads. The hydra has five heads. While it has more than one head, the hydra has advantage on saving throws against being blinded, charmed, deafened, f"
    def hold_breath(self) -> str:
        """Hold Breath: The hydra can hold its breath for 1 hour.Multiple Heads. The hydra has five heads. While it has more..."""
        return "The hydra can hold its breath for 1 hour.Multiple Heads. The hydra has five heads. While it has more than one head, the hydra has advantage on saving throws against being blinded, charmed, deafened, f"

