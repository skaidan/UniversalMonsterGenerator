# bases1/bandit-captain.py
"""
BanditCaptain creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bandit-captain
"""
from creature_base import GlobalCreatureBaseClass


class BanditCaptain(GlobalCreatureBaseClass):
    """
    BanditCaptain creature
    Size: Medium, Type: humanoid (any race), any non-lawful alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 65,
        "min_level": 3,
        "level": 3,
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
        "type": "humanoid (any race), any non-lawful alignment",
        "hit_points_up": [6, 6, 6],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The captain makes three melee attacks: two with its scimitar and one with its dagger. Or the captain..."""
        return "The captain makes three melee attacks: two with its scimitar and one with its dagger. Or the captain makes two ranged attacks with its daggers.Scimitar. Melee Weapon Attack: +5 to hit, reach 5 ft., on"
    def multiattack(self) -> str:
        """Multiattack: The captain makes three melee attacks: two with its scimitar and one with its dagger. Or the captain..."""
        return "The captain makes three melee attacks: two with its scimitar and one with its dagger. Or the captain makes two ranged attacks with its daggers.Scimitar. Melee Weapon Attack: +5 to hit, reach 5 ft., on"

