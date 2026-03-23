# bases1/flind.py
"""
Flind creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flind
"""
from creature_base import GlobalCreatureBaseClass


class Flind(GlobalCreatureBaseClass):
    """
    Flind creature
    Size: Medium, Type: Fiend (Gnoll), typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 127,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fiend (Gnoll), typically Chaotic Evil",
        "hit_points_up": [12, 12, 12],
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
        self.abilities.extend(['aura_of_blood_thirst'])

    def aura_of_blood_thirst(self) -> str:
        """Aura of Blood Thirst: If the flind isn't incapacitated, any creature with the Rampage trait can make a Bite attack as a bo..."""
        return "If the flind isn't incapacitated, any creature with the Rampage trait can make a Bite attack as a bonus action while within 10 feet of the flind.ActionsMultiattack. The flind makes one Flail of Chaos "

