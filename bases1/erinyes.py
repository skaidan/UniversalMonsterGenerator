# bases1/erinyes.py
"""
Erinyes creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=erinyes
"""
from creature_base import GlobalCreatureBaseClass


class Erinyes(GlobalCreatureBaseClass):
    """
    Erinyes creature
    Size: Medium, Type: fiend (Devil), lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 153,
        "min_level": 13,
        "level": 13,
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
        "type": "fiend (Devil), lawful evil",
        "hit_points_up": [15, 15, 15],
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
        self.abilities.extend(['hellish_weapons'])

    def hellish_weapons(self) -> str:
        """Hellish Weapons: The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included..."""
        return "The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included in the attacks).Magic Resistance. The erinyes has advantage on saving throws against spells and oth"
    def hellish_weapons(self) -> str:
        """Hellish Weapons: The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included..."""
        return "The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included in the attacks).Magic Resistance. The erinyes has advantage on saving throws against spells and oth"

