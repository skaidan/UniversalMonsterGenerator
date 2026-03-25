# bases1/goristro.py
"""
Goristro creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=goristro
"""
from creature_base import GlobalCreatureBaseClass


class Goristro(GlobalCreatureBaseClass):
    """
    Huge fiend (Demon) creature - Goristro
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 310, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 11, 'CON': 25, 'INT': 6, 'WIS': 13, 'CHAR': 14, 'armor_class': 19, 'alignment': 'chaotic evil Armor Class  19 (natural armor) Hit Points  310 (23d12 + 161) Speed  40 ft. STR 25 (+7) DEX 11 (+0) CON 25 (+7) INT 6 (-2) WIS 13 (+1) CHA 14 (+2) Saving Throws  Str +13', 'legendary': False, 'size': 'Huge', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'multiattack', 'fist', 'hoof', 'gore']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the goristro moves at least 15 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 38 (7d10) piercing damage. If the target is a creature, """
        return 'If the goristro moves at least 15 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 38 (7d10) piercing damage. If the target is a creature, '

    def multiattack_attack(self) -> str:
        """The goristro makes three attacks: two with its fists and one with its hoof."""
        return 'The goristro makes three attacks: two with its fists and one with its hoof.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage.'

    def hoof_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 23 (3d10 + 7) bludgeoning damage. If the target is a creature, it must succeed on a DC 21 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 23 (3d10 + 7) bludgeoning damage. If the target is a creature, it must succeed on a DC 21 Strength saving throw or be knocked prone.'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 45 (7d10 + 7) piercing damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 45 (7d10 + 7) piercing damage.'

