# bases1/priest.py
"""
Priest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=priest
"""
from creature_base import GlobalCreatureBaseClass


class Priest(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Priest
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 10, 'CON': 12, 'INT': 13, 'WIS': 16, 'CHAR': 13, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 (chain shirt) Hit Points  27 (5d8 + 5) Speed  30 ft. STR 10 (+0) DEX 10 (+0) CON 12 (+1) INT 13 (+1) WIS 16 (+3) CHA 13 (+1) Skills  Medicine +7', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['divine_eminence', 'mace']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def divine_eminence(self) -> str:
        """As a bonus action, the priest can expend a spell slot to cause its melee weapon attacks to magically deal an extra 10 (3d6) radiant damage to a target on a hit. This benefit lasts until the end of the"""
        return 'As a bonus action, the priest can expend a spell slot to cause its melee weapon attacks to magically deal an extra 10 (3d6) radiant damage to a target on a hit. This benefit lasts until the end of the'

    def mace_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage.'

