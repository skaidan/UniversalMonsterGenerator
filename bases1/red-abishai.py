# bases1/red-abishai.py
"""
RedAbishai creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=red-abishai
"""
from creature_base import GlobalCreatureBaseClass


class RedAbishai(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - RedAbishai
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 289, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 16, 'CON': 19, 'INT': 14, 'WIS': 15, 'CHAR': 19, 'armor_class': 22, 'alignment': 'typically Lawful Evil Armor Class  22 (natural armor) Hit Points  289 (34d8 + 136) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'bite', 'claw', 'frightful_presence', 'incite_fanaticism', 'power_of_the_dragon_queen']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The abishai makes one Bite attack and one Claw attack, and it can use Frightful Presence or Incite Fanaticism."""
        return 'The abishai makes one Bite attack and one Claw attack, and it can use Frightful Presence or Incite Fanaticism.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 22 (3d10 + 6) piercing damage plus 38 (7d10) fire damage."""
        return 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 22 (3d10 + 6) piercing damage plus 38 (7d10) fire damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 17 (2d10 + 6) force damage plus 11 (2d10) fire damage."""
        return 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 17 (2d10 + 6) force damage plus 11 (2d10) fire damage.'

    def frightful_presence_attack(self) -> str:
        """Each creature of the abishai's choice that is within 120 feet and aware of the abishai must succeed on a DC 18 Wisdom saving throw or become frightened of it for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the abishai's Frightful Presence for the next 24 hours."""
        return "Each creature of the abishai's choice that is within 120 feet and aware of the abishai must succeed on a DC 18 Wisdom saving throw or become frightened of it for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the abishai's Frightful Presence for the next 24 hours."

    def incite_fanaticism_attack(self) -> str:
        """The abishai chooses up to four other creatures within 60 feet of it that can see it. Until the start of the abishai's next turn, each of those creatures makes attack rolls with advantage and can't be frightened."""
        return "The abishai chooses up to four other creatures within 60 feet of it that can see it. Until the start of the abishai's next turn, each of those creatures makes attack rolls with advantage and can't be frightened."

    def power_of_the_dragon_queen_attack(self) -> str:
        """The abishai targets one Dragon it can see within 120 feet of it. The Dragon must make a DC 18 Charisma saving throw. A chromatic dragon makes this save with disadvantage. On a successful save, the target is immune to the abishai's Power of the Dragon Queen for 1 hour. On a failed save, the target is charmed by the abishai for 1 hour. While charmed in this way, the target regards the abishai as a trusted friend to be heeded and protected. This effect ends if the abishai or its companions deal damage to the target."""
        return "The abishai targets one Dragon it can see within 120 feet of it. The Dragon must make a DC 18 Charisma saving throw. A chromatic dragon makes this save with disadvantage. On a successful save, the target is immune to the abishai's Power of the Dragon Queen for 1 hour. On a failed save, the target is charmed by the abishai for 1 hour. While charmed in this way, the target regards the abishai as a trusted friend to be heeded and protected. This effect ends if the abishai or its companions deal damage to the target."

