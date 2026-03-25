# bases1/devourer.py
"""
Devourer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=devourer
"""
from creature_base import GlobalCreatureBaseClass


class Devourer(GlobalCreatureBaseClass):
    """
    Large Undead creature - Devourer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 12, 'CON': 20, 'INT': 13, 'WIS': 10, 'CHAR': 16, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  189 (18d10 + 90) Speed  30 ft. STR 20 (+5) DEX 12 (+1) CON 20 (+5) INT 13 (+1) WIS 10 (+0) CHA 16 (+3) Damage Resistances  cold', 'legendary': False, 'size': 'Large', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['unusual_nature', 'multiattack', 'claw', 'imprison_soul', 'soul_rend_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def unusual_nature(self) -> str:
        """A devourer doesn't require air, drink, or sleep."""
        return "A devourer doesn't require air, drink, or sleep."

    def multiattack_attack(self) -> str:
        """The devourer makes two Claw attacks and can use either Imprison Soul or Soul Rend, if available."""
        return 'The devourer makes two Claw attacks and can use either Imprison Soul or Soul Rend, if available.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 21 (6d6) necrotic damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 21 (6d6) necrotic damage.'

    def imprison_soul_attack(self) -> str:
        """The devourer chooses a living Humanoid with 0 hit points that it can see within 30 feet of it. That creature is teleported inside the devourer's ribcage and imprisoned there. While imprisoned in this way, the creature is restrained and has disadvantage on death saving throws. If the creature dies while imprisoned, the devourer regains 25 hit points and immediately recharges Soul Rend. Additionally, at the start of its next turn, the devourer regurgitates the slain creature as a bonus action, and the creature becomes an undead. If the victim had 2 or fewer Hit Dice, it becomes a zombie. If it had 3 to 5 Hit Dice, it becomes a ghoul. Otherwise, it becomes a wight. A devourer can imprison only one creature at a time."""
        return "The devourer chooses a living Humanoid with 0 hit points that it can see within 30 feet of it. That creature is teleported inside the devourer's ribcage and imprisoned there. While imprisoned in this way, the creature is restrained and has disadvantage on death saving throws. If the creature dies while imprisoned, the devourer regains 25 hit points and immediately recharges Soul Rend. Additionally, at the start of its next turn, the devourer regurgitates the slain creature as a bonus action, and the creature becomes an undead. If the victim had 2 or fewer Hit Dice, it becomes a zombie. If it had 3 to 5 Hit Dice, it becomes a ghoul. Otherwise, it becomes a wight. A devourer can imprison only one creature at a time."

    def soul_rend_(recharge_6)_attack(self) -> str:
        """The devourer creates a vortex of life-draining energy in a 20-foot radius centered on itself. Each creature in that area must make a DC 18 Constitution saving throw, taking 44 (8d10) necrotic damage on a failed save, or half as much damage on a successful one."""
        return 'The devourer creates a vortex of life-draining energy in a 20-foot radius centered on itself. Each creature in that area must make a DC 18 Constitution saving throw, taking 44 (8d10) necrotic damage on a failed save, or half as much damage on a successful one.'

