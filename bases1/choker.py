# bases1/choker.py
"""
Choker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=choker
"""
from creature_base import GlobalCreatureBaseClass


class Choker(GlobalCreatureBaseClass):
    """
    Small Aberration creature - Choker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 13, 'INT': 4, 'WIS': 12, 'CHAR': 7, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  13 (3d6 + 3) Speed  30 ft. STR 16 (+3) DEX 14 (+2) CON 13 (+1) INT 4 (-3) WIS 12 (+1) CHA 7 (-2) Skills  Stealth +6 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aberrant_quickness_(recharges_after_a_short_or_long_rest)', 'multiattack', 'tentacle']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aberrant_quickness_(recharges_after_a_short_or_long_rest)(self) -> str:
        """The choker can take an extra action on its turn.Boneless. The choker can move through and occupy a space as narrow as 4 inches wide without squeezing.Spider Climb. The choker can climb difficult surfa"""
        return 'The choker can take an extra action on its turn.Boneless. The choker can move through and occupy a space as narrow as 4 inches wide without squeezing.Spider Climb. The choker can climb difficult surfa'

    def multiattack_attack(self) -> str:
        """The choker makes two Tentacle attacks."""
        return 'The choker makes two Tentacle attacks.'

    def tentacle_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 5 (1d4 + 3) piercing damage. If the target is a Large or smaller creature, it is grappled (escape DC 15). Until this grapple ends, the target is restrained, and the choker can't use this tentacle on another target. The choker has two tentacles. If this attack is a critical hit, the target also can't breathe or speak until the grapple ends."""
        return "Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 5 (1d4 + 3) piercing damage. If the target is a Large or smaller creature, it is grappled (escape DC 15). Until this grapple ends, the target is restrained, and the choker can't use this tentacle on another target. The choker has two tentacles. If this attack is a critical hit, the target also can't breathe or speak until the grapple ends."

