# bases1/narzugon.py
"""
Narzugon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=narzugon
"""
from creature_base import GlobalCreatureBaseClass


class Narzugon(GlobalCreatureBaseClass):
    """
    Narzugon creature
    Size: Medium, Type: Fiend (Devil), typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 112,
        "min_level": 14,
        "level": 14,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fiend (Devil), typically Lawful Evil",
        "hit_points_up": [11, 11, 11],
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
        self.abilities.extend(['infernal_tack'])

    def infernal_tack(self) -> str:
        """Infernal Tack: The narzugon wears spurs that are part of infernal tack, which allow it to summon its nightmare comp..."""
        return "The narzugon wears spurs that are part of infernal tack, which allow it to summon its nightmare companion as an action.Magic Resistance. The narzugon has advantage on saving throws against spells and "

