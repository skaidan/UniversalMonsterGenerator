# bases1/shoosuva.py
"""
Shoosuva creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shoosuva
"""
from creature_base import GlobalCreatureBaseClass


class Shoosuva(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - Shoosuva
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 17, 'INT': 7, 'WIS': 14, 'CHAR': 9, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (natural armor) Hit Points  136 (16d10 + 48) Speed  40 ft. STR 18 (+4) DEX 13 (+1) CON 17 (+3) INT 7 (-2) WIS 14 (+2) CHA 9 (-1) Saving Throws  Dex +4', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'tail_stinger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The shoosuva makes one Bite attack and one Tail Stinger attack."""
        return 'The shoosuva makes one Bite attack and one Tail Stinger attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 26 (4d10 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 26 (4d10 + 4) piercing damage.'

    def tail_stinger_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 15 ft., one creature. Hit: 13 (2d8 + 4) piercing damage, and the target must succeed on a DC 14 Constitution saving throw or become poisoned. While poisoned in this way, the target is also paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +7 to hit, reach 15 ft., one creature. Hit: 13 (2d8 + 4) piercing damage, and the target must succeed on a DC 14 Constitution saving throw or become poisoned. While poisoned in this way, the target is also paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

