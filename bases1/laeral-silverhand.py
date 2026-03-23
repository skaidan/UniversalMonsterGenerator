# bases1/laeral-silverhand.py
"""
LaeralSilverhand creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=laeral-silverhand
"""
from creature_base import GlobalCreatureBaseClass


class LaeralSilverhand(GlobalCreatureBaseClass):
    """
    LaeralSilverhand creature
    Size: Medium, Type: humanoid (Human), chaotic good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 228,
        "min_level": 18,
        "level": 18,
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
        "type": "humanoid (Human), chaotic good",
        "hit_points_up": [22, 22, 22],
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
        """Special Equipment: Laeral wears a white robe of the archmagi (accounted for in her statistics). She wields a flame tong..."""
        return "Laeral wears a white robe of the archmagi (accounted for in her statistics). She wields a flame tongue longsword.Magic Resistance. While wearing her robe of the archmagi, Laeral has advantage on savin"

