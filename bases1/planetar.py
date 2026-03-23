# bases1/planetar.py
"""
Planetar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=planetar
"""
from creature_base import GlobalCreatureBaseClass


class Planetar(GlobalCreatureBaseClass):
    """
    Planetar creature
    Size: Large, Type: celestial, lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 200,
        "min_level": 17,
        "level": 17,
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
        "type": "celestial, lawful good",
        "hit_points_up": [20, 20, 20],
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
        self.abilities.extend(['angelic_weapons'])

    def angelic_weapons(self) -> str:
        """Angelic Weapons: The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals ..."""
        return "The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals an extra 5d8 radiant damage (included in the attack).Divine Awareness. The planetar knows if it hear"
    def angelic_weapons(self) -> str:
        """Angelic Weapons: The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals ..."""
        return "The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals an extra 5d8 radiant damage (included in the attack).Divine Awareness. The planetar knows if it hear"

