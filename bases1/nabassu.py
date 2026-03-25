# bases1/nabassu.py
"""
Nabassu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nabassu
"""
from creature_base import GlobalCreatureBaseClass


class Nabassu(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Nabassu
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 190, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 14, 'CON': 21, 'INT': 14, 'WIS': 15, 'CHAR': 17, 'armor_class': 18, 'alignment': 'typically Chaotic Evil Armor Class  18 (natural armor) Hit Points  190 (20d8 + 100) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['demonic_shadows', 'multiattack', 'bite', 'claw', 'soul-stealing_gaze']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def demonic_shadows(self) -> str:
        """The nabassu darkens the area around its body in a 10-foot radius. Nonmagical light can't illuminate this area of dim light.Devour Soul. A nabassu can eat the soul of a creature it has killed within th"""
        return "The nabassu darkens the area around its body in a 10-foot radius. Nonmagical light can't illuminate this area of dim light.Devour Soul. A nabassu can eat the soul of a creature it has killed within th"

    def multiattack_attack(self) -> str:
        """The nabassu makes one Bite attack and one Claw attack, and it uses Soul-Stealing Gaze."""
        return 'The nabassu makes one Bite attack and one Claw attack, and it uses Soul-Stealing Gaze.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 38 (5d12 + 6) necrotic damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 38 (5d12 + 6) necrotic damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 28 (4d10 + 6) force damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 28 (4d10 + 6) force damage.'

    def soul-stealing_gaze_attack(self) -> str:
        """The nabassu targets one creature it can see within 30 feet of it. If the target isn't a Construct or an Undead, it must succeed on a DC 16 Charisma saving throw or take 13 (2d12) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage dealt, and the nabassu regains hit points equal to half that amount. This reduction lasts until the target finishes a short or long rest. The target dies if its hit point maximum is reduced to 0, and if the target is a Humanoid, it immediately rises as a ghoul under the nabassu's control."""
        return "The nabassu targets one creature it can see within 30 feet of it. If the target isn't a Construct or an Undead, it must succeed on a DC 16 Charisma saving throw or take 13 (2d12) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage dealt, and the nabassu regains hit points equal to half that amount. This reduction lasts until the target finishes a short or long rest. The target dies if its hit point maximum is reduced to 0, and if the target is a Humanoid, it immediately rises as a ghoul under the nabassu's control."

