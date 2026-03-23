# bases1/alustriel-silverhand.py
"""
AlustrielSilverhand creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=alustriel-silverhand
"""
from creature_base import GlobalCreatureBaseClass


class AlustrielSilverhand(GlobalCreatureBaseClass):
    """
    AlustrielSilverhand creature
    Size: Medium, Type: Humanoid (Human, Wizard), Chaotic Good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 272,
        "min_level": 22,
        "level": 22,
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
        "type": "Humanoid (Human, Wizard), Chaotic Good",
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
        self.abilities.extend(['ear_of_the_chosen'])

    def ear_of_the_chosen(self) -> str:
        """Ear of the Chosen: Whenever a creature on the same plane of existence as Alustriel speaks Alustriel's name, Alustriel h..."""
        return "Whenever a creature on the same plane of existence as Alustriel speaks Alustriel's name, Alustriel hearsher name and the next nine words the speaker utters.Legendary Resistance (3/Day). If Alustriel f"

