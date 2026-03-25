# bases1/grung-elite-warrior.py
"""
GrungEliteWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grung-elite-warrior
"""
from creature_base import GlobalCreatureBaseClass


class GrungEliteWarrior(GlobalCreatureBaseClass):
    """
    Small Humanoid creature - GrungEliteWarrior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 49, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 16, 'CON': 15, 'INT': 10, 'WIS': 11, 'CHAR': 12, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 Hit Points  49 (9d6 + 18) Speed  25 ft.', 'legendary': False, 'size': 'Small', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'dagger', 'shortbow', 'mesmerizing_chirr_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw """
        return "The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw "

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 5 (2d4) poison damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 5 (2d4) poison damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 5 (2d4) poison damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 5 (2d4) poison damage.'

    def mesmerizing_chirr_(recharge_6)_attack(self) -> str:
        """The grung makes a chirring noise to which grungs are immune. Each Humanoid or Beast that is within 15 feet of the grung and able to hear it must succeed on a DC 12 Wisdom saving throw or be stunned until the end of the grung's next turn."""
        return "The grung makes a chirring noise to which grungs are immune. Each Humanoid or Beast that is within 15 feet of the grung and able to hear it must succeed on a DC 12 Wisdom saving throw or be stunned until the end of the grung's next turn."

