# bases1/kuo-toa-whip.py
"""
KuoToaWhip creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kuo-toa-whip
"""
from creature_base import GlobalCreatureBaseClass


class KuoToaWhip(GlobalCreatureBaseClass):
    """
    KuoToaWhip creature
    Size: Medium, Type: or smaller creature, it is grappled (escape DC 14). Until this grapple ends, the kuo-toa can't use its pincer staff on another target.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 65,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller creature, it is grappled (escape DC 14). Until this grapple ends, the kuo-toa can't use its pincer staff on another target.",
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of..."""
        return "The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such "
    def amphibious(self) -> str:
        """Amphibious: The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of..."""
        return "The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such "

