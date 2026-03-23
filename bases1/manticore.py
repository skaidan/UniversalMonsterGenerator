# bases1/manticore.py
"""
Manticore creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=manticore
"""
from creature_base import GlobalCreatureBaseClass


class Manticore(GlobalCreatureBaseClass):
    """
    Manticore creature
    Size: Large, Type: monstrosity, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 68,
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
        "size": "Large",
        "type": "monstrosity, lawful evil",
        "hit_points_up": [6, 6, 6],
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
        self.abilities.extend(['tail_spike_regrowth'])

    def tail_spike_regrowth(self) -> str:
        """Tail Spike Regrowth: The manticore has twenty-four tail spikes. Used spikes regrow when the manticore finishes a long res..."""
        return "The manticore has twenty-four tail spikes. Used spikes regrow when the manticore finishes a long rest.ActionsMultiattack. The manticore makes three attacks: one with its bite and two with its claws or"
    def tail_spike_regrowth(self) -> str:
        """Tail Spike Regrowth: The manticore has twenty-four tail spikes. Used spikes regrow when the manticore finishes a long res..."""
        return "The manticore has twenty-four tail spikes. Used spikes regrow when the manticore finishes a long rest.ActionsMultiattack. The manticore makes three attacks: one with its bite and two with its claws or"

