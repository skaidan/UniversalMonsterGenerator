# bases1/firenewt-warrior.py
"""
FirenewtWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=firenewt-warrior
"""
from creature_base import GlobalCreatureBaseClass


class FirenewtWarrior(GlobalCreatureBaseClass):
    """
    FirenewtWarrior creature
    Size: Medium, Type: Elemental, typically Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 27,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Elemental, typically Neutral",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The firenewt can breathe air and water.ActionsMultiattack. The firenewt makes two Scimitar attacks.S..."""
        return "The firenewt can breathe air and water.ActionsMultiattack. The firenewt makes two Scimitar attacks.Scimitar. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.S"

