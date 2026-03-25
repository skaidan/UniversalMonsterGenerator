# bases1/erinyes.py
"""
Erinyes creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=erinyes
"""
from creature_base import GlobalCreatureBaseClass


class Erinyes(GlobalCreatureBaseClass):
    """
    Medium fiend (Devil) creature - Erinyes
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 153, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 16, 'CON': 18, 'INT': 14, 'WIS': 14, 'CHAR': 18, 'armor_class': 18, 'alignment': 'lawful evil Armor Class  18 (plate) Hit Points  153 (18d8 + 72) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hellish_weapons', 'multiattack', 'longsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hellish_weapons(self) -> str:
        """The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included in the attacks).Magic Resistance. The erinyes has advantage on saving throws against spells and oth"""
        return "The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included in the attacks).Magic Resistance. The erinyes has advantage on saving throws against spells and oth"

    def multiattack_attack(self) -> str:
        """The erinyes makes three attacks."""
        return 'The erinyes makes three attacks.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands, plus 13 (3d8) poison damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands, plus 13 (3d8) poison damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 13 (3d8) poison damage, and the target must succeed on a DC 14 Constitution saving throw or be poisoned. The poison lasts until it is removed by the lesser restoration spell or similar magic."""
        return 'Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 13 (3d8) poison damage, and the target must succeed on a DC 14 Constitution saving throw or be poisoned. The poison lasts until it is removed by the lesser restoration spell or similar magic.'

