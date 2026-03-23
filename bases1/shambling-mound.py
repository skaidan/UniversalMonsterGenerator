# bases1/shambling-mound.py
"""
ShamblingMound creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shambling-mound
"""
from creature_base import GlobalCreatureBaseClass


class ShamblingMound(GlobalCreatureBaseClass):
    """
    ShamblingMound creature
    Size: Medium, Type: or smaller creature grappled by it. The engulfed target is blinded, restrained, and unable to breathe, and it must succeed on a DC 14 Constitution saving throw at the start of each of the mound's turns or take 13 (2d8 + 4) bludgeoning damage. If the mound moves, the engulfed target moves with it. The mound can have only one creature engulfed at a time.
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
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature grappled by it. The engulfed target is blinded, restrained, and unable to breathe, and it must succeed on a DC 14 Constitution saving throw at the start of each of the mound's turns or take 13 (2d8 + 4) bludgeoning damage. If the mound moves, the engulfed target moves with it. The mound can have only one creature engulfed at a time.",
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
        self.abilities.extend(['lightning_absorption'])

    def lightning_absorption(self) -> str:
        """Lightning Absorption: Whenever the shambling mound is subjected to lightning damage, it takes no damage and regains a numb..."""
        return "Whenever the shambling mound is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt.ActionsMultiattack. The shambling mound makes t"
    def lightning_absorption(self) -> str:
        """Lightning Absorption: Whenever the shambling mound is subjected to lightning damage, it takes no damage and regains a numb..."""
        return "Whenever the shambling mound is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt.ActionsMultiattack. The shambling mound makes t"

