# bases1/roc.py
"""
Roc creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=roc
"""
from creature_base import GlobalCreatureBaseClass


class Roc(GlobalCreatureBaseClass):
    """
    Gargantuan monstrosity creature - Roc
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 248, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 10, 'CON': 20, 'INT': 3, 'WIS': 10, 'CHAR': 9, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  248 (16d20 + 80) Speed  20 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'multiattack', 'beak', 'talons']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The roc has advantage on Wisdom (Perception) checks that rely on sight."""
        return 'The roc has advantage on Wisdom (Perception) checks that rely on sight.'

    def multiattack_attack(self) -> str:
        """The roc makes two attacks: one with its beak and one with its talons."""
        return 'The roc makes two attacks: one with its beak and one with its talons.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 27 (4d8 + 9) piercing damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 27 (4d8 + 9) piercing damage.'

    def talons_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 23 (4d6 + 9) slashing damage, and the target is grappled (escape DC 19). Until this grapple ends, the target is restrained, and the roc can't use its talons on another target."""
        return "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 23 (4d6 + 9) slashing damage, and the target is grappled (escape DC 19). Until this grapple ends, the target is restrained, and the roc can't use its talons on another target."

