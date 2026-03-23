# bases1/vecna-the-archlich.py
"""
VecnaTheArchlich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vecna-the-archlich
"""
from creature_base import GlobalCreatureBaseClass


class VecnaTheArchlich(GlobalCreatureBaseClass):
    """
    VecnaTheArchlich creature
    Size: Medium, Type: Undead (Wizard), Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 272,
        "min_level": 27,
        "level": 27,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Undead (Wizard), Lawful Evil",
        "hit_points_up": [27, 27, 27],
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
        self.abilities.extend(['legendary_resistance_day'])

    def legendary_resistance_day(self) -> str:
        """Legendary Resistance (5/Day): If Vecna fails a saving throw, he can choose to succeed instead.Special Equipment. Vecna carries a m..."""
        return "If Vecna fails a saving throw, he can choose to succeed instead.Special Equipment. Vecna carries a magic dagger named Afterthought. In the hands of anyone other than Vecna, Afterthought is a +2 dagger"

