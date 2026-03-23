# bases1/warrior-lvl-2.py
"""
WarriorLvl2 creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warrior-lvl-2
"""
from creature_base import GlobalCreatureBaseClass


class WarriorLvl2(GlobalCreatureBaseClass):
    """
    WarriorLvl2 creature
    Size: Medium, Type: humanoid (any race), -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 19,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), -",
        "hit_points_up": [1, 1, 1],
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
        self.abilities.extend(['martial_role'])

    def martial_role(self) -> str:
        """Martial Role: The warrior has one of the following traits of your choice:Attacker. The warrior gains a +2 bonus to..."""
        return "The warrior has one of the following traits of your choice:Attacker. The warrior gains a +2 bonus to attack rolls.Defender. The warrior gains the Protection reaction below.Second Wind. The warrior can"

