# bases1/nabassu.py
"""
Nabassu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nabassu
"""
from creature_base import GlobalCreatureBaseClass


class Nabassu(GlobalCreatureBaseClass):
    """
    Nabassu creature
    Size: Medium, Type: Fiend (Demon), typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 190,
        "min_level": 16,
        "level": 16,
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
        "type": "Fiend (Demon), typically Chaotic Evil",
        "hit_points_up": [19, 19, 19],
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
        self.abilities.extend(['demonic_shadows'])

    def demonic_shadows(self) -> str:
        """Demonic Shadows: The nabassu darkens the area around its body in a 10-foot radius. Nonmagical light can't illuminate ..."""
        return "The nabassu darkens the area around its body in a 10-foot radius. Nonmagical light can't illuminate this area of dim light.Devour Soul. A nabassu can eat the soul of a creature it has killed within th"

