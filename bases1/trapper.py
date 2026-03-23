# bases1/trapper.py
"""
Trapper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=trapper
"""
from creature_base import GlobalCreatureBaseClass


class Trapper(GlobalCreatureBaseClass):
    """
    Trapper creature
    Size: Large, Type: or smaller creature within 10 feet of the trapper must succeed on a DC 13 Dexterity saving throw or be grappled (escape DC 14). Until the grapple ends, the target takes 13 (3d6 + 3) bludgeoning damage plus 3 (1d6) acid damage at the start of each of its turns. While grappled in this way, the target is restrained, blinded, and deprived of air. The trapper can smother only one creature at a time.
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
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "or smaller creature within 10 feet of the trapper must succeed on a DC 13 Dexterity saving throw or be grappled (escape DC 14). Until the grapple ends, the target takes 13 (3d6 + 3) bludgeoning damage plus 3 (1d6) acid damage at the start of each of its turns. While grappled in this way, the target is restrained, blinded, and deprived of air. The trapper can smother only one creature at a time.",
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
        # Add creature-specific abilities
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: If the trapper is motionless on a floor, wall, or ceiling at the start of combat, it has advantage o..."""
        return "If the trapper is motionless on a floor, wall, or ceiling at the start of combat, it has advantage on its initiative roll. Moreover, if a creature hasn't observed the trapper move or act, that creatur"

