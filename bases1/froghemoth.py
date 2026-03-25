# bases1/froghemoth.py
"""
Froghemoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=froghemoth
"""
from creature_base import GlobalCreatureBaseClass


class Froghemoth(GlobalCreatureBaseClass):
    """
    Huge Monstrosity creature - Froghemoth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 161, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 13, 'CON': 20, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  161 (14d12 + 70) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'bite', 'tentacle', 'tongue']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The froghemoth can breathe air and water.Shock Susceptibility. If the froghemoth takes lightning damage, it suffers two effects until the end of its next turn: its speed is halved, and it has disadvan"""
        return 'The froghemoth can breathe air and water.Shock Susceptibility. If the froghemoth takes lightning damage, it suffers two effects until the end of its next turn: its speed is halved, and it has disadvan'

    def multiattack_attack(self) -> str:
        """The froghemoth makes one Bite attack and two Tentacle attacks, and it can use Tongue."""
        return 'The froghemoth makes one Bite attack and two Tentacle attacks, and it can use Tongue.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 22 (3d10 + 6) piercing damage, and the target is swallowed if it is a Medium or smaller creature. A swallowed creature is blinded and restrained, has total cover against attacks and other effects outside the froghemoth, and takes 10 (3d6) acid damage at the start of each of the froghemoth's turns. The froghemoth's gullet can hold up to two creatures at a time. If the froghemoth takes 20 damage or more on a single turn from a creature inside it, the froghemoth must succeed on a DC 20 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, each of which falls prone in a space within 10 feet of the froghemoth. If the froghemoth dies, any swallowed creature is no longer restrained by it and can escape from the corpse using 10 feet of movement, exiting prone."""
        return "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 22 (3d10 + 6) piercing damage, and the target is swallowed if it is a Medium or smaller creature. A swallowed creature is blinded and restrained, has total cover against attacks and other effects outside the froghemoth, and takes 10 (3d6) acid damage at the start of each of the froghemoth's turns. The froghemoth's gullet can hold up to two creatures at a time. If the froghemoth takes 20 damage or more on a single turn from a creature inside it, the froghemoth must succeed on a DC 20 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, each of which falls prone in a space within 10 feet of the froghemoth. If the froghemoth dies, any swallowed creature is no longer restrained by it and can escape from the corpse using 10 feet of movement, exiting prone."

    def tentacle_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 20 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage, and the target is grappled (escape DC 16) if it is a Huge or smaller creature. Until the grapple ends, the froghemoth can't use this tentacle on another target. The froghemoth has four tentacles."""
        return "Melee Weapon Attack: +10 to hit, reach 20 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage, and the target is grappled (escape DC 16) if it is a Huge or smaller creature. Until the grapple ends, the froghemoth can't use this tentacle on another target. The froghemoth has four tentacles."

    def tongue_attack(self) -> str:
        """The froghemoth targets one Medium or smaller creature that it can see within 20 feet of it. The target must make a DC 18 Strength saving throw. On a failed save, the target is pulled into an unoccupied space within 5 feet of the froghemoth."""
        return 'The froghemoth targets one Medium or smaller creature that it can see within 20 feet of it. The target must make a DC 18 Strength saving throw. On a failed save, the target is pulled into an unoccupied space within 5 feet of the froghemoth.'

