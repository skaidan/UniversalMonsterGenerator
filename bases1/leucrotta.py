# bases1/leucrotta.py
"""
Leucrotta creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=leucrotta
"""
from creature_base import GlobalCreatureBaseClass


class Leucrotta(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - Leucrotta
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 15, 'INT': 9, 'WIS': 12, 'CHAR': 6, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (natural armor) Hit Points  67 (9d10 + 18) Speed  50 ft. STR 18 (+4) DEX 14 (+2) CON 15 (+2) INT 9 (-1) WIS 12 (+1) CHA 6 (-2) Skills  Deception +2', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['mimicry', 'multiattack', 'bite', 'hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def mimicry(self) -> str:
        """The leucrotta can mimic Beast sounds and Humanoid voices. A creature that hears the sounds can tell they are imitations only with a successful DC 14 Wisdom (Insight) check.Stench. Any creature other t"""
        return 'The leucrotta can mimic Beast sounds and Humanoid voices. A creature that hears the sounds can tell they are imitations only with a successful DC 14 Wisdom (Insight) check.Stench. Any creature other t'

    def multiattack_attack(self) -> str:
        """The leucrotta makes one Bite attack and one Hooves attack."""
        return 'The leucrotta makes one Bite attack and one Hooves attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage. If the leucrotta scores a critical hit, it rolls the damage dice three times, instead of twice."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage. If the leucrotta scores a critical hit, it rolls the damage dice three times, instead of twice.'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

