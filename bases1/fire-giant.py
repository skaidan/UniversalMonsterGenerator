# bases1/fire-giant.py
"""
FireGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-giant
"""
from creature_base import GlobalCreatureBaseClass


class FireGiant(GlobalCreatureBaseClass):
    """
    FireGiant creature
    Size: Huge, Type: giant, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 162,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "giant, lawful evil",
        "hit_points_up": [16, 16, 16],
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
        """Multiattack: The giant makes two greatsword attacks.Greatsword. Melee Weapon Attack: +11 to hit, reach 10 ft., on..."""
        return "The giant makes two greatsword attacks.Greatsword. Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 28 (6d6 + 7) slashing damage.Rock. Ranged Weapon Attack: +11 to hit, range 60/240 ft."
    def multiattack(self) -> str:
        """Multiattack: The giant makes two greatsword attacks.Greatsword. Melee Weapon Attack: +11 to hit, reach 10 ft., on..."""
        return "The giant makes two greatsword attacks.Greatsword. Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 28 (6d6 + 7) slashing damage.Rock. Ranged Weapon Attack: +11 to hit, range 60/240 ft."

