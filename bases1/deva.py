# bases1/deva.py
"""
Deva creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deva
"""
from creature_base import GlobalCreatureBaseClass


class Deva(GlobalCreatureBaseClass):
    """
    Deva creature
    Size: Medium, Type: celestial, lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 136,
        "min_level": 11,
        "level": 11,
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
        "type": "celestial, lawful good",
        "hit_points_up": [13, 13, 13],
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
        """Angelic Weapons: The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra..."""
        return "The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra 4d8 radiant damage (included in the attack).Innate Spellcasting. The deva's spellcasting ability is"
    def angelic_weapons(self) -> str:
        """Angelic Weapons: The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra..."""
        return "The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra 4d8 radiant damage (included in the attack).Innate Spellcasting. The deva's spellcasting ability is"

