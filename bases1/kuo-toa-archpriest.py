# bases1/kuo-toa-archpriest.py
"""
KuoToaArchpriest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kuo-toa-archpriest
"""
from creature_base import GlobalCreatureBaseClass


class KuoToaArchpriest(GlobalCreatureBaseClass):
    """
    KuoToaArchpriest creature
    Size: Medium, Type: humanoid (Kuo-toa), neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 97,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (Kuo-toa), neutral evil",
        "hit_points_up": [9, 9, 9],
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

