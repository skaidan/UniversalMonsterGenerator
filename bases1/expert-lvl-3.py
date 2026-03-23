# bases1/expert-lvl-3.py
"""
ExpertLvl3 creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=expert-lvl-3
"""
from creature_base import GlobalCreatureBaseClass


class ExpertLvl3(GlobalCreatureBaseClass):
    """
    ExpertLvl3 creature
    Size: Medium, Type: humanoid (any race), -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 1,
        "level": 1,
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
        "type": "humanoid (any race), -",
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
        # Add creature-specific abilities
        self.abilities.extend(['helpful'])

    def helpful(self) -> str:
        """Helpful: The expert can take the Help action as a bonus action.Tools. The expert has thieves' tools and a mus..."""
        return "The expert can take the Help action as a bonus action.Tools. The expert has thieves' tools and a musical instrument.Cunning Action. On the expert's turn in combat, it can take the Dash, Disengage, or "

