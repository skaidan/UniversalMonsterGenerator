# bases1/vine-blight.py
"""
VineBlight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vine-blight
"""
from creature_base import GlobalCreatureBaseClass


class VineBlight(GlobalCreatureBaseClass):
    """
    Medium plant creature - VineBlight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 8, 'CON': 14, 'INT': 5, 'WIS': 10, 'CHAR': 3, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 (natural armor) Hit Points  26 (4d8 + 8) Speed  10 ft. STR 15 (+2) DEX 8 (-1) CON 14 (+2) INT 5 (-3) WIS 10 (+0) CHA 3 (-4) Skills  Stealth + 1 Condition Immunities  blinded', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'constrict', 'entangling_plants_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the blight remains motionless, it is indistinguishable from a tangle of vines."""
        return 'While the blight remains motionless, it is indistinguishable from a tangle of vines.'

    def constrict_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage, and a Large or smaller target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the blight can't constrict another target."""
        return "Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage, and a Large or smaller target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the blight can't constrict another target."

    def entangling_plants_(recharge_5-6)_attack(self) -> str:
        """Grasping roots and vines sprout in a 15-foot radius centered on the blight, withering away after 1 minute. For the duration, that area is difficult terrain for nonplant creatures. In addition, each creature of the blight's choice in that area when the plants appear must succeed on a DC 12 Strength saving throw or become restrained. A creature can use its action to make a DC 12 Strength check, freeing it self or another entangled creature within reach on a success."""
        return "Grasping roots and vines sprout in a 15-foot radius centered on the blight, withering away after 1 minute. For the duration, that area is difficult terrain for nonplant creatures. In addition, each creature of the blight's choice in that area when the plants appear must succeed on a DC 12 Strength saving throw or become restrained. A creature can use its action to make a DC 12 Strength check, freeing it self or another entangled creature within reach on a success."

