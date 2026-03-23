# bases1/shoosuva.py
"""
Shoosuva creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shoosuva
"""
from creature_base import GlobalCreatureBaseClass


class Shoosuva(GlobalCreatureBaseClass):
    """
    Shoosuva creature
    Size: Large, Type: Fiend (Demon), typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 136,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Fiend (Demon), typically Chaotic Evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The shoosuva makes one Bite attack and one Tail Stinger attack.Bite. Melee Weapon Attack: +7 to hit,..."""
        return "The shoosuva makes one Bite attack and one Tail Stinger attack.Bite. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 26 (4d10 + 4) piercing damage.Tail Stinger. Melee Weapon Attack: +7 t"

