# bases1/flind.py
"""
Flind creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flind
"""
from creature_base import GlobalCreatureBaseClass


class Flind(GlobalCreatureBaseClass):
    """
    Medium Fiend (Gnoll) creature - Flind
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 14, 'CON': 19, 'INT': 11, 'WIS': 13, 'CHAR': 12, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (breastplate) Hit Points  127 (15d8 + 60) Speed  30 ft. STR 20 (+5) DEX 14 (+2) CON 19 (+4) INT 11 (+0) WIS 13 (+1) CHA 12 (+1) Saving Throws  Con +8', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Gnoll)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aura_of_blood_thirst', 'multiattack', 'flail_of_chaos', 'flail_of_pain', 'flail_of_paralysis', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aura_of_blood_thirst(self) -> str:
        """If the flind isn't incapacitated, any creature with the Rampage trait can make a Bite attack as a bonus action while within 10 feet of the flind."""
        return "If the flind isn't incapacitated, any creature with the Rampage trait can make a Bite attack as a bonus action while within 10 feet of the flind."

    def multiattack_attack(self) -> str:
        """The flind makes one Flail of Chaos attack, one Flail of Pain attack, and one Flail of Paralysis attack, or it makes three Longbow attacks."""
        return 'The flind makes one Flail of Chaos attack, one Flail of Pain attack, and one Flail of Paralysis attack, or it makes three Longbow attacks.'

    def flail_of_chaos_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) bludgeoning damage, and the target must make a DC 16 Wisdom saving throw. On a failed save, the target must use its reaction, if available, to make one melee attack against a random creature, other than the flind, within its reach. If there's no creature within reach, the target instead moves half its speed in a random direction."""
        return "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) bludgeoning damage, and the target must make a DC 16 Wisdom saving throw. On a failed save, the target must use its reaction, if available, to make one melee attack against a random creature, other than the flind, within its reach. If there's no creature within reach, the target instead moves half its speed in a random direction."

    def flail_of_pain_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) bludgeoning damage plus 16 (3d10) psychic damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) bludgeoning damage plus 16 (3d10) psychic damage.'

    def flail_of_paralysis_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) bludgeoning damage, and the target must succeed on a DC 16 Constitution saving throw or be paralyzed until the end of its next turn."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) bludgeoning damage, and the target must succeed on a DC 16 Constitution saving throw or be paralyzed until the end of its next turn.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

