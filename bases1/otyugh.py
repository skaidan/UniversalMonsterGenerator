# bases1/otyugh.py
"""
Otyugh creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=otyugh
"""
from creature_base import GlobalCreatureBaseClass


class Otyugh(GlobalCreatureBaseClass):
    """
    Large aberration creature - Otyugh
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 114, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 19, 'INT': 6, 'WIS': 13, 'CHAR': 6, 'armor_class': 14, 'alignment': 'neutral Armor Class  14 (natural armor) Hit Points  114 (12d10 + 48) Speed  30 ft. STR 16 (+3) DEX 11 (+0) CON 19 (+4) INT 6 (-2) WIS 13 (+1) CHA 6 (-2) Saving Throws  Con +7 Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Large', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['limited_telepathy', 'multiattack', 'bite', 'tentacle', 'tentacle_slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def limited_telepathy(self) -> str:
        """The otyugh can magically transmit simple messages and images to any creature within 120 feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepa"""
        return "The otyugh can magically transmit simple messages and images to any creature within 120 feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepa"

    def multiattack_attack(self) -> str:
        """The otyugh makes three attacks: one with its bite and two with its tentacles."""
        return 'The otyugh makes three attacks: one with its bite and two with its tentacles.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the target must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. The disease is cured on a success. The target dies if the disease reduces its hit point maximum to 0. This reduction to the target's hit point maximum lasts until the disease is cured."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the target must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. The disease is cured on a success. The target dies if the disease reduces its hit point maximum to 0. This reduction to the target's hit point maximum lasts until the disease is cured."

    def tentacle_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage plus 4 (1d8) piercing damage. If the target is Medium or smaller, it is grappled (escape DC 13) and restrained until the grapple ends. The otyugh has two tentacles, each of which can grapple one target."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage plus 4 (1d8) piercing damage. If the target is Medium or smaller, it is grappled (escape DC 13) and restrained until the grapple ends. The otyugh has two tentacles, each of which can grapple one target.'

    def tentacle_slam_attack(self) -> str:
        """The otyugh slams creatures grappled by it into each other or a solid surface. Each creature must succeed on a DC 14 Constitution saving throw or take 10 (2d6 + 3) bludgeoning damage and be stunned until the end of the otyugh's next turn. On a successful save, the target takes half the bludgeoning damage and isn't stunned."""
        return "The otyugh slams creatures grappled by it into each other or a solid surface. Each creature must succeed on a DC 14 Constitution saving throw or take 10 (2d6 + 3) bludgeoning damage and be stunned until the end of the otyugh's next turn. On a successful save, the target takes half the bludgeoning damage and isn't stunned."

