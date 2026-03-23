# bases1/raven.py
"""
Raven creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=raven
"""
from creature_base import GlobalCreatureBaseClass


class Raven(GlobalCreatureBaseClass):
    """
    Raven creature
    Size: Tiny, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 1,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "beast, unaligned",
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
        self.abilities.extend(['mimicry'])

    def mimicry(self) -> str:
        """Mimicry: The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an an..."""
        return "The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC "
    def mimicry(self) -> str:
        """Mimicry: The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an an..."""
        return "The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC "

