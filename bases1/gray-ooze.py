# bases1/gray-ooze.py
"""
GrayOoze creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gray-ooze
"""
from creature_base import GlobalCreatureBaseClass


class GrayOoze(GlobalCreatureBaseClass):
    """
    Medium ooze creature - GrayOoze
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 6, 'CON': 16, 'INT': 1, 'WIS': 6, 'CHAR': 2, 'armor_class': 8, 'alignment': 'unaligned Armor Class  8 Hit Points  22 (3d8 + 9) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amorphous', 'pseudopod']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amorphous(self) -> str:
        """The ooze can move through a space as narrow as 1 inch wide without squeezing.Corrode Metal. Any nonmagical weapon made of metal that hits the ooze corrodes. After dealing damage, the weapon takes a pe"""
        return 'The ooze can move through a space as narrow as 1 inch wide without squeezing.Corrode Metal. Any nonmagical weapon made of metal that hits the ooze corrodes. After dealing damage, the weapon takes a pe'

    def pseudopod_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage plus 7 (2d6) acid damage, and if the target is wearing nonmagical metal armor, its armor is partly corroded and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage plus 7 (2d6) acid damage, and if the target is wearing nonmagical metal armor, its armor is partly corroded and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10.'

