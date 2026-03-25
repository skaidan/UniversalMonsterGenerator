# bases1/purple-worm.py
"""
PurpleWorm creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=purple-worm
"""
from creature_base import GlobalCreatureBaseClass


class PurpleWorm(GlobalCreatureBaseClass):
    """
    Gargantuan monstrosity creature - PurpleWorm
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 247, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 7, 'CON': 22, 'INT': 1, 'WIS': 8, 'CHAR': 4, 'armor_class': 18, 'alignment': 'unaligned Armor Class  18 (natural armor) Hit Points  247 (15d20 + 90) Speed  50 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['tunneler', 'multiattack', 'bite', 'tail_stinger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def tunneler(self) -> str:
        """The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel in its wake."""
        return 'The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel in its wake.'

    def multiattack_attack(self) -> str:
        """The worm makes two attacks: one with its bite and one with its stinger."""
        return 'The worm makes two attacks: one with its bite and one with its stinger.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 22 (3d8 + 9) piercing damage. If the target is a Large or smaller creature, it must succeed on a DC 19 Dexterity saving throw or be swallowed by the worm. A swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the worm, and it takes 21 (6d6) acid damage at the start of each of the worm's turns. If the worm takes 30 damage or more on a single turn from a creature inside it, the worm must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the worm. If the worm dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 20 feet of movement, exiting prone."""
        return "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 22 (3d8 + 9) piercing damage. If the target is a Large or smaller creature, it must succeed on a DC 19 Dexterity saving throw or be swallowed by the worm. A swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the worm, and it takes 21 (6d6) acid damage at the start of each of the worm's turns. If the worm takes 30 damage or more on a single turn from a creature inside it, the worm must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the worm. If the worm dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 20 feet of movement, exiting prone."

    def tail_stinger_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one creature. Hit: 19 (3d6 + 9) piercing damage, and the target must make a DC 19 Constitution saving throw, taking 42 (12d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +14 to hit, reach 10 ft., one creature. Hit: 19 (3d6 + 9) piercing damage, and the target must make a DC 19 Constitution saving throw, taking 42 (12d6) poison damage on a failed save, or half as much damage on a successful one.'

