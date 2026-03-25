# bases1/boneclaw.py
"""
Boneclaw creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=boneclaw
"""
from creature_base import GlobalCreatureBaseClass


class Boneclaw(GlobalCreatureBaseClass):
    """
    Large Undead creature - Boneclaw
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 150, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 16, 'CON': 15, 'INT': 13, 'WIS': 15, 'CHAR': 9, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  150 (20d10 + 40) Speed  40 ft. STR 19 (+4) DEX 16 (+3) CON 15 (+2) INT 13 (+1) WIS 15 (+2) CHA 9 (-1) Saving Throws  Dex +7', 'legendary': False, 'size': 'Large', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['rejuvenation', 'multiattack', 'piercing_claw', 'shadow_jump_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def rejuvenation(self) -> str:
        """While its master lives, a destroyed boneclaw gains a new body in 1d10 hours, with all its hit points. The new body appears within 1 mile of the boneclaw's master.Unusual Nature. The boneclaw doesn't r"""
        return "While its master lives, a destroyed boneclaw gains a new body in 1d10 hours, with all its hit points. The new body appears within 1 mile of the boneclaw's master.Unusual Nature. The boneclaw doesn't r"

    def multiattack_attack(self) -> str:
        """The boneclaw makes two Piercing Claw attacks."""
        return 'The boneclaw makes two Piercing Claw attacks.'

    def piercing_claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 15 ft., one target. Hit: 20 (3d10 + 4) piercing damage plus 11 (2d10) necrotic damage. If the target is a creature, the boneclaw can pull the target up to 10 feet toward itself, and the target is grappled (escape DC 14). The boneclaw has two claws. While a claw grapples a target, the claw can attack only that target."""
        return 'Melee Weapon Attack: +8 to hit, reach 15 ft., one target. Hit: 20 (3d10 + 4) piercing damage plus 11 (2d10) necrotic damage. If the target is a creature, the boneclaw can pull the target up to 10 feet toward itself, and the target is grappled (escape DC 14). The boneclaw has two claws. While a claw grapples a target, the claw can attack only that target.'

    def shadow_jump_(recharge_5–6)_attack(self) -> str:
        """If the boneclaw is in dim light or darkness, each creature of the boneclaw's choice within 15 feet of it must succeed on a DC 14 Constitution saving throw or take 34 (5d12 + 2) necrotic damage. The boneclaw then teleports up to 60 feet to an unoccupied space it can see. It can bring one creature it's grappling, teleporting that creature to an unoccupied space it can see within 5 feet of its destination. The destination spaces of this teleportation must be in dim light or darkness."""
        return "If the boneclaw is in dim light or darkness, each creature of the boneclaw's choice within 15 feet of it must succeed on a DC 14 Constitution saving throw or take 34 (5d12 + 2) necrotic damage. The boneclaw then teleports up to 60 feet to an unoccupied space it can see. It can bring one creature it's grappling, teleporting that creature to an unoccupied space it can see within 5 feet of its destination. The destination spaces of this teleportation must be in dim light or darkness."

