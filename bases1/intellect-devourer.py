# bases1/intellect-devourer.py
"""
IntellectDevourer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=intellect-devourer
"""
from creature_base import GlobalCreatureBaseClass


class IntellectDevourer(GlobalCreatureBaseClass):
    """
    Tiny aberration creature - IntellectDevourer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 21, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 14, 'CON': 13, 'INT': 12, 'WIS': 11, 'CHAR': 10, 'armor_class': 12, 'alignment': 'lawful evil Armor Class  12 Hit Points  21 (6d4 + 6) Speed  40 ft. STR 6 (-2) DEX 14 (+2) CON 13 (+1) INT 12 (+1) WIS 11 (+0) CHA 10 (+0) Skills  Perception +2', 'legendary': False, 'size': 'Tiny', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['detect_sentience', 'multiattack', 'claws', 'devour_intellect', 'body_thief']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def detect_sentience(self) -> str:
        """The intellect devourer can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is pro"""
        return 'The intellect devourer can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is pro'

    def multiattack_attack(self) -> str:
        """The intellect devourer makes one attack with its claws and uses Devour Intellect."""
        return 'The intellect devourer makes one attack with its claws and uses Devour Intellect.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage.'

    def devour_intellect_attack(self) -> str:
        """The intellect devourer targets one creature it can see within 10 feet of it that has a brain. The target must succeed on a DC 12 Intelligence saving throw against this magic or take 11 (2d10) psychic damage. Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. The target is stunned until it regains at least one point of Intelligence."""
        return "The intellect devourer targets one creature it can see within 10 feet of it that has a brain. The target must succeed on a DC 12 Intelligence saving throw against this magic or take 11 (2d10) psychic damage. Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. The target is stunned until it regains at least one point of Intelligence."

    def body_thief_attack(self) -> str:
        """The intellect devourer initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good. If it wins the contest, the intellect devourer magically consumes the target's brain, teleports into the target's skull, and takes control of the target's body. While inside a creature, the intellect devourer has total cover against attacks and other effects originating outs ide its host. The intellect devourer retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of Deep Speech, its telepathy, and its traits. It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages. If the host body die, the intellect devourer must leave it. A protection from evil and good spell cast on the body drives the intellect devourer out. The intellect devourer is also forced out if the target regains its devoured brain by means of a wish. By spending 5 feet of its movement, the intellect devourer can voluntarily leave the body, teleporting to the nearest unoccupied space within 5 feet of it. The body then dies, unless its brain is restored within 1 round."""
        return "The intellect devourer initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good. If it wins the contest, the intellect devourer magically consumes the target's brain, teleports into the target's skull, and takes control of the target's body. While inside a creature, the intellect devourer has total cover against attacks and other effects originating outs ide its host. The intellect devourer retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of Deep Speech, its telepathy, and its traits. It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages. If the host body die, the intellect devourer must leave it. A protection from evil and good spell cast on the body drives the intellect devourer out. The intellect devourer is also forced out if the target regains its devoured brain by means of a wish. By spending 5 feet of its movement, the intellect devourer can voluntarily leave the body, teleporting to the nearest unoccupied space within 5 feet of it. The body then dies, unless its brain is restored within 1 round."

