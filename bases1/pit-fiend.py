# bases1/pit-fiend.py
"""
PitFiend creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pit-fiend
"""
from creature_base import GlobalCreatureBaseClass


class PitFiend(GlobalCreatureBaseClass):
    """
    PitFiend creature
    Size: Large, Type: fiend (Devil), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 300,
        "min_level": 21,
        "level": 21,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend (Devil), lawful evil",
        "hit_points_up": [30, 30, 30],
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
        self.abilities.extend(['fear_aura'])

    def fear_aura(self) -> str:
        """Fear Aura: Any creature hostile to the pit fiend that starts its turn within 20 feet of the pit fiend must make..."""
        return "Any creature hostile to the pit fiend that starts its turn within 20 feet of the pit fiend must make a DC 21 Wisdom saving throw, unless the pit fiend is incapacitated. On a failed save, the creature "
    def fear_aura(self) -> str:
        """Fear Aura: Any creature hostile to the pit fiend that starts its turn within 20 feet of the pit fiend must make..."""
        return "Any creature hostile to the pit fiend that starts its turn within 20 feet of the pit fiend must make a DC 21 Wisdom saving throw, unless the pit fiend is incapacitated. On a failed save, the creature "

