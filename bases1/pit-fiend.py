# bases1/pit-fiend.py
"""
PitFiend creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pit-fiend
"""
from creature_base import GlobalCreatureBaseClass


class PitFiend(GlobalCreatureBaseClass):
    """
    Large fiend (Devil) creature - PitFiend
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 300, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 14, 'CON': 24, 'INT': 22, 'WIS': 18, 'CHAR': 24, 'armor_class': 19, 'alignment': 'lawful evil Armor Class  19 (natural armor) Hit Points  300 (24d10 + 168) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fear_aura', 'multiattack', 'bite', 'claw', 'mace', 'tail']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fear_aura(self) -> str:
        """Any creature hostile to the pit fiend that starts its turn within 20 feet of the pit fiend must make a DC 21 Wisdom saving throw, unless the pit fiend is incapacitated. On a failed save, the creature """
        return 'Any creature hostile to the pit fiend that starts its turn within 20 feet of the pit fiend must make a DC 21 Wisdom saving throw, unless the pit fiend is incapacitated. On a failed save, the creature '

    def multiattack_attack(self) -> str:
        """The pit fiend makes four attacks: one with its bite, one with its claw, one with its mace, and one with its tail."""
        return 'The pit fiend makes four attacks: one with its bite, one with its claw, one with its mace, and one with its tail.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 5 ft., one target. Hit: 22 (4d6 + 8) piercing damage. The target must succeed on a DC 21 Constitution saving throw or become poisoned. While poisoned in this way, the target can't regain hit points, and it takes 21 (6d6) poison damage at the start of each of its turns. The poisoned target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return "Melee Weapon Attack: +14 to hit, reach 5 ft., one target. Hit: 22 (4d6 + 8) piercing damage. The target must succeed on a DC 21 Constitution saving throw or become poisoned. While poisoned in this way, the target can't regain hit points, and it takes 21 (6d6) poison damage at the start of each of its turns. The poisoned target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 17 (2d8 + 8) slashing damage."""
        return 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 17 (2d8 + 8) slashing damage.'

    def mace_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 15 (2d6 + 8) bludgeoning damage plus 21 (6d6) fire damage."""
        return 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 15 (2d6 + 8) bludgeoning damage plus 21 (6d6) fire damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 24 (3d10 + 8) bludgeoning damage."""
        return 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 24 (3d10 + 8) bludgeoning damage.'

