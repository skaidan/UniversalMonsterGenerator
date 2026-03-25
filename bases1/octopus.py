# bases1/octopus.py
"""
Octopus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=octopus
"""
from creature_base import GlobalCreatureBaseClass


class Octopus(GlobalCreatureBaseClass):
    """
    Small beast creature - Octopus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 3, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 15, 'CON': 11, 'INT': 3, 'WIS': 10, 'CHAR': 4, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  3 (1d6) Speed  5 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'tentacles', 'ink_cloud_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """While out of water, the octopus can hold its breath for 30 minutes.Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.Water Breathing. The octopus can"""
        return 'While out of water, the octopus can hold its breath for 30 minutes.Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.Water Breathing. The octopus can'

    def tentacles_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage, and the target is grappled (escape DC 10). Until this grapple ends, the octopus can't use its tentacles on another target."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage, and the target is grappled (escape DC 10). Until this grapple ends, the octopus can't use its tentacles on another target."

    def ink_cloud_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """A 5-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action."""
        return 'A 5-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action.'

