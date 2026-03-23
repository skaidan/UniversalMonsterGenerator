# bases1/drow-shadowblade.py
"""
DrowShadowblade creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-shadowblade
"""
from creature_base import GlobalCreatureBaseClass


class DrowShadowblade(GlobalCreatureBaseClass):
    """
    DrowShadowblade creature
    Size: Medium, Type: Humanoid (Elf), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 150,
        "min_level": 12,
        "level": 12,
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
        "type": "Humanoid (Elf), any alignment",
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
        # Add creature-specific abilities
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the drow's darkvision.Fey Ancestry. The drow has advantage on saving..."""
        return "Magical darkness doesn't impede the drow's darkvision.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in "

