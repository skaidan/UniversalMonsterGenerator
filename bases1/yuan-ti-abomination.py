# bases1/yuan-ti-abomination.py
"""
YuanTiAbomination creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-abomination
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiAbomination(GlobalCreatureBaseClass):
    """
    Large monstrosity (Shapechanger creature - YuanTiAbomination
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 16, 'CON': 17, 'INT': 17, 'WIS': 15, 'CHAR': 18, 'armor_class': 15, 'alignment': 'Yuan-ti)', 'legendary': False, 'size': 'Large', 'type': 'monstrosity (Shapechanger', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack_(abomination_form_only)', 'bite', 'constrict', 'scimitar_(abomination_form_only)', 'longbow_(abomination_form_only)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The yuan-ti can use its action to polymorph into a Large snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It does"""
        return "The yuan-ti can use its action to polymorph into a Large snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It does"

    def multiattack_(abomination_form_only)_attack(self) -> str:
        """The yuan-ti makes two ranged attacks or three melee attacks, but can use its bite and constrict attacks only once each."""
        return 'The yuan-ti makes two ranged attacks or three melee attacks, but can use its bite and constrict attacks only once each.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 7 (1d6 + 4) piercing damage plus 10 (3d6) poison damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 7 (1d6 + 4) piercing damage plus 10 (3d6) poison damage.'

    def constrict_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the target is restrained, and the yuan-ti can't constrict another target."""
        return "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the target is restrained, and the yuan-ti can't constrict another target."

    def scimitar_(abomination_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.'

    def longbow_(abomination_form_only)_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 12 (2d8 + 3) piercing damage plus 10 (3d6) poison damage."""
        return 'Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 12 (2d8 + 3) piercing damage plus 10 (3d6) poison damage.'

