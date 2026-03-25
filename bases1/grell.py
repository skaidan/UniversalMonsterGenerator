# bases1/grell.py
"""
Grell creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grell
"""
from creature_base import GlobalCreatureBaseClass


class Grell(GlobalCreatureBaseClass):
    """
    Medium aberration creature - Grell
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 55, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 13, 'INT': 12, 'WIS': 11, 'CHAR': 9, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 Hit Points  55 (10d8 + 10) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'tentacles', 'beak']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The grell makes two attacks: one with its tentacles and one with its beak."""
        return 'The grell makes two attacks: one with its tentacles and one with its beak.'

    def tentacles_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or be poisoned for 1 minute. The poisoned target is paralyzed, and it can repeat the saving throw at the end of each of its turns, ending the effect on a success. The target is also grappled (escape DC 15). If the target is Medium or smaller, it is also restrained until this grapple ends. While grappling the target, the grell has advantage on attack rolls against it and can't use this attack against other targets. When the grell moves, any Medium or smaller target it is grappling moves with it."""
        return "Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or be poisoned for 1 minute. The poisoned target is paralyzed, and it can repeat the saving throw at the end of each of its turns, ending the effect on a success. The target is also grappled (escape DC 15). If the target is Medium or smaller, it is also restrained until this grapple ends. While grappling the target, the grell has advantage on attack rolls against it and can't use this attack against other targets. When the grell moves, any Medium or smaller target it is grappling moves with it."

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage.'

