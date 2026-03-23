# bases1/drow-matron-mother.py
"""
DrowMatronMother creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-matron-mother
"""
from creature_base import GlobalCreatureBaseClass


class DrowMatronMother(GlobalCreatureBaseClass):
    """
    DrowMatronMother creature
    Size: Medium, Type: Humanoid (Cleric, Elf), typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 247,
        "min_level": 21,
        "level": 21,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid (Cleric, Elf), typically Neutral Evil",
        "hit_points_up": [24, 24, 24],
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
        self.abilities.extend(['special_equipment'])

    def special_equipment(self) -> str:
        """Special Equipment: The drow wields a tentacle rod.Fey Ancestry. The drow has advantage on saving throws against being c..."""
        return "The drow wields a tentacle rod.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in sunlight, the drow has "

