# bases1/expert-lvl-1.py
"""
ExpertLvl1 creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=expert-lvl-1
"""
from creature_base import GlobalCreatureBaseClass


class ExpertLvl1(GlobalCreatureBaseClass):
    """
    ExpertLvl1 creature
    Size: Medium, Type: humanoid (any race), -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
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
        "hit_points_up": [1, 1, 1],
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
        return "The expert can take the Help action as a bonus action.Tools. The expert has thieves' tools and a musical instrument.ActionsShortsword. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 ("

