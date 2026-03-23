# bases1/blackguard.py
"""
Blackguard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blackguard
"""
from creature_base import GlobalCreatureBaseClass


class Blackguard(GlobalCreatureBaseClass):
    """
    Blackguard creature
    Size: Medium, Type: Humanoid (Paladin), typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 119,
        "min_level": 9,
        "level": 9,
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
        "type": "Humanoid (Paladin), typically Neutral Evil",
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The blackguard makes three attacks, using Glaive, Shortbow, or both.Glaive. Melee Weapon Attack: +7 ..."""
        return "The blackguard makes three attacks, using Glaive, Shortbow, or both.Glaive. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) slashing damage plus 9 (2d8) necrotic damage.Sho"

