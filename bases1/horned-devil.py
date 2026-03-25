# bases1/horned-devil.py
"""
HornedDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=horned-devil
"""
from creature_base import GlobalCreatureBaseClass


class HornedDevil(GlobalCreatureBaseClass):
    """
    Large fiend (Devil) creature - HornedDevil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 178, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 17, 'CON': 21, 'INT': 12, 'WIS': 16, 'CHAR': 17, 'armor_class': 18, 'alignment': 'lawful evil Armor Class  18 (natural armor) Hit Points  178 (17d10 + 85) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'fork', 'tail', 'hurl_flame']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The devil makes three melee attacks: two with its fork and one with its tail. It can use Hurl Flame in place of any melee attack."""
        return 'The devil makes three melee attacks: two with its fork and one with its tail. It can use Hurl Flame in place of any melee attack.'

    def fork_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 15 (2d8 + 6) piercing damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 15 (2d8 + 6) piercing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 10 (1d8 + 6) piercing damage. If the target is a creature other than an undead or a construct, it must succeed on a DC 17 Constitution saving throw or lose 10 (3d6) hit points at the start of each of its turns due to an infernal wound. Each time the devil hits the wounded target with this attack, the damage dealt by the wound increases by 10 (3d6). Any creature can take an action to stanch the wound with a successful DC 12 Wisdom (Medicine) check. The wound also closes if the target receives magical healing."""
        return 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 10 (1d8 + 6) piercing damage. If the target is a creature other than an undead or a construct, it must succeed on a DC 17 Constitution saving throw or lose 10 (3d6) hit points at the start of each of its turns due to an infernal wound. Each time the devil hits the wounded target with this attack, the damage dealt by the wound increases by 10 (3d6). Any creature can take an action to stanch the wound with a successful DC 12 Wisdom (Medicine) check. The wound also closes if the target receives magical healing.'

    def hurl_flame_attack(self) -> str:
        """Ranged Spell Attack: +7 to hit, range 150 ft., one target. Hit: 14 (4d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire."""
        return "Ranged Spell Attack: +7 to hit, range 150 ft., one target. Hit: 14 (4d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire."

