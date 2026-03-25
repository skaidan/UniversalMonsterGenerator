# bases1/tanarukk.py
"""
Tanarukk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tanarukk
"""
from creature_base import GlobalCreatureBaseClass


class Tanarukk(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Tanarukk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 95, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 20, 'INT': 9, 'WIS': 9, 'CHAR': 9, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (natural armor) Hit Points  95 (10d8 + 50) Speed  30 ft. STR 18 (+4) DEX 13 (+1) CON 20 (+5) INT 9 (-1) WIS 9 (-1) CHA 9 (-1) Skills  Intimidation +2', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'bite', 'greatsword']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The tanarukk has advantage on saving throws against spells and other magical effects."""
        return 'The tanarukk has advantage on saving throws against spells and other magical effects.'

    def multiattack_attack(self) -> str:
        """The tanarukk makes one Bite attack and one Greatsword attack."""
        return 'The tanarukk makes one Bite attack and one Greatsword attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.'

