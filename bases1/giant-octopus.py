# bases1/giant-octopus.py
"""
GiantOctopus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-octopus
"""
from creature_base import GlobalCreatureBaseClass


class GiantOctopus(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantOctopus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 13, 'CON': 13, 'INT': 4, 'WIS': 10, 'CHAR': 4, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  52 (8d10 + 8) Speed  10 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'tentacles', 'ink_cloud_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """While out of water, the octopus can hold its breath for 1 hour.Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.Water Breathing. The octopus can bre"""
        return 'While out of water, the octopus can hold its breath for 1 hour.Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.Water Breathing. The octopus can bre'

    def tentacles_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 15 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage. If the target is a creature, it is grappled (escape DC 16). Until this grapple ends, the target is restrained, and the octopus can't use its tentacles on another target."""
        return "Melee Weapon Attack: +5 to hit, reach 15 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage. If the target is a creature, it is grappled (escape DC 16). Until this grapple ends, the target is restrained, and the octopus can't use its tentacles on another target."

    def ink_cloud_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """A 20-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action."""
        return 'A 20-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action.'

