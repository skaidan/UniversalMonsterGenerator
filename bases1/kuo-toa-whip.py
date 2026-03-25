# bases1/kuo-toa-whip.py
"""
KuoToaWhip creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kuo-toa-whip
"""
from creature_base import GlobalCreatureBaseClass


class KuoToaWhip(GlobalCreatureBaseClass):
    """
    Medium humanoid (Kuo-toa) creature - KuoToaWhip
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 65, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 10, 'CON': 14, 'INT': 12, 'WIS': 14, 'CHAR': 11, 'armor_class': 11, 'alignment': 'neutral evil Armor Class  11 (natural armor) Hit Points  65 (10d8 + 20) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Kuo-toa)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'bite', 'pincer_staff']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such """
        return 'The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such '

    def multiattack_attack(self) -> str:
        """The kuo-toa makes two attacks: one with its bite and one with its pincer staff."""
        return 'The kuo-toa makes two attacks: one with its bite and one with its pincer staff.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def pincer_staff_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 5 (1d6 + 2) piercing damage. If the target is a Medium or smaller creature, it is grappled (escape DC 14). Until this grapple ends, the kuo-toa can't use its pincer staff on another target."""
        return "Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 5 (1d6 + 2) piercing damage. If the target is a Medium or smaller creature, it is grappled (escape DC 14). Until this grapple ends, the kuo-toa can't use its pincer staff on another target."

