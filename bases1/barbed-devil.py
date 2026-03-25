# bases1/barbed-devil.py
"""
BarbedDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=barbed-devil
"""
from creature_base import GlobalCreatureBaseClass


class BarbedDevil(GlobalCreatureBaseClass):
    """
    Medium fiend (Devil) creature - BarbedDevil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 110, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 17, 'CON': 18, 'INT': 12, 'WIS': 14, 'CHAR': 14, 'armor_class': 15, 'alignment': 'lawful evil Armor Class  15 (natural armor) Hit Points  110 (13d8 + 52) Speed  30 ft. STR 16 (+3) DEX 17 (+3) CON 18 (+4) INT 12 (+1) WIS 14 (+2) CHA 14 (+2) Saving Throws  Str +6', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['barbed_hide', 'multiattack', 'claw', 'tail', 'hurl_flame']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def barbed_hide(self) -> str:
        """At the start of each of its turns, the barbed devil deals 5 (1d10) piercing damage to any creature grappling it.Devil's Sight. Magical darkness doesn't impede the devil's darkvision.Magic Resistance. """
        return "At the start of each of its turns, the barbed devil deals 5 (1d10) piercing damage to any creature grappling it.Devil's Sight. Magical darkness doesn't impede the devil's darkvision.Magic Resistance. "

    def multiattack_attack(self) -> str:
        """The devil makes three melee attacks: one with its tail and two with its claws. Alternatively, it can use Hurl Flame twice."""
        return 'The devil makes three melee attacks: one with its tail and two with its claws. Alternatively, it can use Hurl Flame twice.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage.'

    def hurl_flame_attack(self) -> str:
        """Ranged Spell Attack: +5 to hit, range 150 ft., one target. Hit: 10 (3d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire."""
        return "Ranged Spell Attack: +5 to hit, range 150 ft., one target. Hit: 10 (3d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire."

