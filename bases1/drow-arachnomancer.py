# bases1/drow-arachnomancer.py
"""
DrowArachnomancer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-arachnomancer
"""
from creature_base import GlobalCreatureBaseClass


class DrowArachnomancer(GlobalCreatureBaseClass):
    """
    DrowArachnomancer creature
    Size: Large, Type: spider, remaining in that form for up to 1 hour, or back into its true form. Its statistics, other than its size, are the same in each form. It can speak and cast spells while in spider form. Any equipment it is wearing or carrying in Humanoid form melds into the spider form. It can't activate, use, wield, or otherwise benefit from any of its equipment. It reverts to its Humanoid form if it dies.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 162,
        "min_level": 14,
        "level": 14,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "spider, remaining in that form for up to 1 hour, or back into its true form. Its statistics, other than its size, are the same in each form. It can speak and cast spells while in spider form. Any equipment it is wearing or carrying in Humanoid form melds into the spider form. It can't activate, use, wield, or otherwise benefit from any of its equipment. It reverts to its Humanoid form if it dies.",
        "hit_points_up": [16, 16, 16],
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
        self.abilities.extend(['fey_ancestry'])

    def fey_ancestry(self) -> str:
        """Fey Ancestry: The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep..."""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Spider Climb. The drow can climb difficult surfaces, including upside down on ceilings, without nee"

