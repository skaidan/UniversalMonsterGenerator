# bases1/giant-frog.py
"""
GiantFrog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-frog
"""
from creature_base import GlobalCreatureBaseClass


class GiantFrog(GlobalCreatureBaseClass):
    """
    Medium beast creature - GiantFrog
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 13, 'CON': 11, 'INT': 2, 'WIS': 10, 'CHAR': 3, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  18 (4d8) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'bite', 'swallow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The frog can breathe air and water.Standing Leap. The frog's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."""
        return "The frog can breathe air and water.Standing Leap. The frog's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage, and the target is grappled (escape DC 11). Until this grapple ends, the target is restrained, and the frog can't bite another target."""
        return "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage, and the target is grappled (escape DC 11). Until this grapple ends, the target is restrained, and the frog can't bite another target."

    def swallow_attack(self) -> str:
        """The frog makes one bite attack against a Small or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the frog, and it takes 5 (2d4) acid damage at the start of each of the frog's turns. The frog can have only one target swallowed at a time. If the frog dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."""
        return "The frog makes one bite attack against a Small or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the frog, and it takes 5 (2d4) acid damage at the start of each of the frog's turns. The frog can have only one target swallowed at a time. If the frog dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."

