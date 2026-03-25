# bases1/black-pudding.py
"""
BlackPudding creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=black-pudding
"""
from creature_base import GlobalCreatureBaseClass


class BlackPudding(GlobalCreatureBaseClass):
    """
    Large ooze creature - BlackPudding
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 5, 'CON': 16, 'INT': 1, 'WIS': 6, 'CHAR': 1, 'armor_class': 7, 'alignment': 'unaligned Armor Class  7 Hit Points  85 (10d10 + 30) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amorphous', 'pseudopod']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amorphous(self) -> str:
        """The pudding can move through a space as narrow as 1 inch wide without squeezing.Corrosive Form. A creature that touches the pudding or hits it with a melee attack while within 5 feet of it takes 4 (1d"""
        return 'The pudding can move through a space as narrow as 1 inch wide without squeezing.Corrosive Form. A creature that touches the pudding or hits it with a melee attack while within 5 feet of it takes 4 (1d'

    def pseudopod_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage plus 18 (4d8) acid damage. In addition, nonmagical armor worn by the target is partly dissolved and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage plus 18 (4d8) acid damage. In addition, nonmagical armor worn by the target is partly dissolved and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10.'

