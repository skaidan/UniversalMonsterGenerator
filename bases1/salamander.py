# bases1/salamander.py
"""
Salamander creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=salamander
"""
from creature_base import GlobalCreatureBaseClass


class Salamander(GlobalCreatureBaseClass):
    """
    Large elemental creature - Salamander
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 15, 'INT': 11, 'WIS': 10, 'CHAR': 12, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (natural armor) Hit Points  90 (12d10 + 24) Speed  30 ft. STR 18 (+4) DEX 14 (+2) CON 15 (+2) INT 11 (+0) WIS 10 (+0) CHA 12 (+1) Damage Vulnerabilities  cold Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['heated_body', 'multiattack', 'spear', 'tail']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def heated_body(self) -> str:
        """A creature that touches the salamander or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.Heated Weapons. Any metal melee weapon the salamander wields deals an extra 3 """
        return 'A creature that touches the salamander or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.Heated Weapons. Any metal melee weapon the salamander wields deals an extra 3 '

    def multiattack_attack(self) -> str:
        """The salamander makes two attacks: one with its spear and one with its tail."""
        return 'The salamander makes two attacks: one with its spear and one with its tail.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20 ft./60 ft., one target. Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage."""
        return 'Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20 ft./60 ft., one target. Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage plus 7 (2d6) fire damage, and the target is grappled (escape DC 14). Until this grapple ends, the target is restrained, the salamander can automatically hit the target with its tail, and the salamander can't make tail attacks against other targets."""
        return "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage plus 7 (2d6) fire damage, and the target is grappled (escape DC 14). Until this grapple ends, the target is restrained, the salamander can automatically hit the target with its tail, and the salamander can't make tail attacks against other targets."

